from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")


class Index(TemplateView):
    template_name = "index.html"

def google_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')


def tutor_check(request):
    return render(request, 'tutorCheck.html')

def StudentView(request):
    return render(request, 'tutorMeStudent.html')

def TutorView(request):
    return render(request, 'tutorMeTutor.html')