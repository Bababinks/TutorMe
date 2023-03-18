from django.db.models import Model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")
from tutorMe import Json
from tutorMe.Json import get_JSON_Subjects, Searchereds
from tutorMe.models import tutorMeUser, TutorClasses
import requests

from django.urls import reverse


def is_tutor(user):
    return tutorMeUser.objects.filter(email=user.email, is_tutor=True).exists()


def is_not_tutor(user):
    return tutorMeUser.objects.filter(email=user.email, is_tutor=False).exists()


def not_student(user):
    return not tutorMeUser.objects.filter(email=user.email, is_tutor=False).exists()


def not_tutor(user):
    return not tutorMeUser.objects.filter(email=user.email, is_tutor=True).exists()


class Index(TemplateView):
    template_name = "index.html"


def google_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')


@login_required
def tutor_check(request):
    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=False).exists():
        return redirect('/tutorMe/student')

    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=True).exists():
        return redirect('/tutorMe/tutor')

    return render(request, 'tutorCheck.html')


@login_required
@user_passes_test(not_student)
def TutorView(request):
    if not tutorMeUser.objects.filter(email=request.user.email, is_tutor=True).exists():
        newuser = tutorMeUser();
        newuser.email = request.user.email
        newuser.is_tutor = True
        newuser.first_name = request.user.first_name
        newuser.last_name = request.user.last_name
        newuser.save()

    if request.method == 'POST':
        initialSearchQuery = request.POST.get("searchBar")

        if initialSearchQuery:
            initialSearchResults = Searchereds(initialSearchQuery)
            return render(request, 'tutorMeTutorClasses.html', {'searchResults': initialSearchResults})
        else:
            return render(request, 'tutorMeTutor.html', )

    return render(request, 'tutorMeTutor.html')


@login_required
@user_passes_test(is_tutor)
def Tutor_Classes_View(request):
    choice = request.POST.get("choice")
    classes = Json.get_classes(choice, "2023", "Spring")

    request.session[0] = choice
    return render(request, 'tutorMeTutorClasses.html', {'classes': classes})


@login_required
@user_passes_test(is_tutor)
def deleteClass(request, Class):
    cur_user = tutorMeUser.objects.get(email=request.user.email)

    mnemonic = Class.split(' ', 1)[0]
    namewithoutmneonic = Class.split(' ', 1)[1]
    query = TutorClasses.objects.filter(name=namewithoutmneonic, tutor_id=cur_user, mnemonic=mnemonic)
    query.delete()

    return Tutor_Classes_List_View(request)

def searchView(request):
    if request.method == 'POST':
        searchQuery = request.POST.get("searchBar")

        if searchQuery:
            searchResults = Searchereds(searchQuery)
        else:
            searchResults = []

    return render(request, 'tutorMeTutorClasses.html', {'searchResults': searchResults})


@login_required
@user_passes_test(is_tutor)
def Tutor_Classes_List_View(request):
    class_choice = request.POST.get("class_choice", "")
    cur_user = tutorMeUser.objects.get(email=request.user.email)
    if class_choice != "":
        mnemonic = request.session['0']

        if not TutorClasses.objects.filter(name=class_choice, tutor=cur_user).exists():
            newclass = TutorClasses();
            newclass.tutor = cur_user
            newclass.mnemonic = mnemonic
            newclass.name = class_choice
            newclass.save()

    query = TutorClasses.objects.filter(tutor=cur_user)

    list = []
    for i in query:
        curmneonic = i.mnemonic
        curname = i.name
        curmneonic += " "
        curmneonic += curname
        list.append(curmneonic)

    return render(request, 'TutorClassList.html', {'list': list})


def addClass(request, mnemonic, name, number):
    print("view called")
    cur_user = tutorMeUser.objects.get(email=request.user.email)
    if not TutorClasses.objects.filter(name=name, tutor=cur_user).exists():
        newclass = TutorClasses();
        newclass.tutor = cur_user
        newclass.mnemonic = mnemonic
        newclass.name = name
        newclass.number = number
        newclass.save()
    return redirect(reverse('tutor_classes_list_view'))


@login_required
@user_passes_test(not_tutor)
def StudentView(request):
    if not tutorMeUser.objects.filter(email=request.user.email, is_tutor=False).exists():
        newuser = tutorMeUser();
        newuser.email = request.user.email
        newuser.is_tutor = False
        newuser.first_name = request.user.first_name
        newuser.last_name = request.user.last_name
        newuser.save()

    items = get_JSON_Subjects("2023", "Spring");

    return render(request, 'tutorMeStudent.html', {'items': items})


@login_required
@user_passes_test(is_not_tutor)
def Student_Classes_View(request):
    choice = request.POST.get("choice")
    # classes = Json.get_classes(choice, "2023", "Spring")
    return render(request, 'tutorMeStudentClasses.html')


@login_required
@user_passes_test(is_not_tutor)
def Student_Classes_List_View(request):
    class_choice = request.POST.get("class_choice")
    query = TutorClasses.objects.filter(name=class_choice)

    list = []
    for i in query:
        tutor = i.tutor
        first = tutor.first_name
        last = tutor.last_name
        full_name = first + " " + last
        list.append(full_name)

    return render(request, 'StudentClassList.html', {'list': list})
