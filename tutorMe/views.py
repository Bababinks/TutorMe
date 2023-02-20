from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView


# def index(request):
#     return HttpResponse("Hello, world. You're at the tutorMe index.")


class Index(TemplateView):
    template_name = "index.html"