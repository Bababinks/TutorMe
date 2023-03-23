from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('tutorMe/logout', LogoutView.as_view()),
    path('tutorCheck/', views.tutor_check),

    path('student', views.StudentView),
    path('tutor', views.TutorView),
    path('delete/<str:Class>/', views.deleteClass, name='delete_item'),
    path('add/<str:mnemonic>/<str:name>/<str:number>/', views.addClass, name='add_item'),
    path('student/classes', views.Student_Classes_View),
    # path('tutor/classes', views.Tutor_Classes_View),

    path('student/classes/list', views.Student_Classes_List_View,  name='student_classes_list_view'),
    path('tutor/classes/list', views.Tutor_Classes_List_View, name='tutor_classes_list_view'),
    path('tutor/classes', views.searchView),
    path('check/<str:mnemonic>/<str:name>/<str:number>/', views.Student_Classes_List_View, name='check'),
    path('tutor/classes/list/<str:name>', views.schedule_view, name='schedule'),
    path('tutor/classes/<str:class_name>/times', views.calendar_times, name='calendar_times'),
]