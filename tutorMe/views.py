from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
import requests



# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")
from tutorMe.models import tutorMeUser


class Index(TemplateView):
    template_name = "index.html"


def google_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')


def tutor_check(request):
    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=False).exists():
        return render(request, 'tutorMeStudent.html')
    if tutorMeUser.objects.filter(email=request.user.email, is_tutor=True).exists():
        return render(request, 'tutorMeTutor.html')

    return render(request, 'tutorCheck.html')


def StudentView(request):
    newuser = tutorMeUser();
    newuser.email = request.user.email
    newuser.is_tutor = False
    newuser.save()

    return render(request, 'tutorMeStudent.html')


def TutorView(request):
    newuser = tutorMeUser();
    newuser.email = request.user.email
    newuser.is_tutor = True
    newuser.save()

    return render(request, 'tutorMeTutor.html')


def searchResults(request):
    if request.method == "POST":
        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1228&page=1&instructor_name=Horton"

        response = requests.get(url)

        data_json = response.json()
        query = request.POST.get("data", "")
        return render(request, 'searchResults.html', {"query": query,"junaid": data_json
                                                      })
    else:
        return render(request, 'searchResults.html')
