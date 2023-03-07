from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")
from tutorMe import Json
from tutorMe.Json import get_JSON_Subjects
from tutorMe.models import tutorMeUser
import requests


class Index(TemplateView):
    template_name = "index.html"


def google_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')


def tutor_check(request):

    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=False).exists():
        return redirect('/tutorMe/student')

    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=True).exists():
        return redirect('/tutorMe/tutor')

    return render(request, 'tutorCheck.html')


def StudentView(request):
    if not tutorMeUser.objects.filter(email=request.user.email, is_tutor=False).exists():
        newuser = tutorMeUser();
        newuser.email = request.user.email
        newuser.is_tutor = False
        newuser.save()

    items = get_JSON_Subjects("2023", "Spring");


    return render(request, 'tutorMeStudent.html', {'items': items})


def TutorView(request):

    if not tutorMeUser.objects.filter(email=request.user.email, is_tutor=True).exists():
        newuser = tutorMeUser();
        newuser.email = request.user.email
        newuser.is_tutor = True
        newuser.save()

    items = get_JSON_Subjects("2023", "Spring");
    return render(request, 'tutorMeTutor.html', {'items': items})


def Student_Classes_View(request):
    choice = request.POST.get("choice")
    classes = Json.get_classes(choice, "2023", "Spring")
    return render(request, 'tutorMeStudentClasses.html', {'classes': classes})

def Tutor_Classes_View(request):
    choice = request.POST.get("choice")
    classes = Json.get_classes(choice, "2023", "Spring")

    return render(request, 'tutorMeTutorClasses.html', {'classes': classes})




