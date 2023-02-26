from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('tutorCheck/',views.tutor_check),


]