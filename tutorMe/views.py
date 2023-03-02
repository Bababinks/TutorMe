import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")
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
    total_classes = []

    response = requests.get(
        "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1228&page=1&instructor_name=Horton").json()
    for aClass in response:
        word = aClass["subject_descr"]
        total_classes.append(word)
        print(word)

    return render(request, 'tutorMeTutor.html', {'response', total_classes})
