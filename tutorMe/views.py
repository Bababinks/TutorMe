from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")
from tutorMe import Json
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
        items = Json.get_JSON_Subjects();
        return render(request, 'tutorMeTutor.html', {'items': items})

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
