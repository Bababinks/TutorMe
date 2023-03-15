from django.contrib import admin

# Register your models here.
from .models import tutorMeUser,Course
admin.site.register(tutorMeUser)


class MyModelAdmin(admin.ModelAdmin):
    list_display =["Subject","course_name","course_number"]
admin.site.register(Course,MyModelAdmin)

