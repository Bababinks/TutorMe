from django.contrib import admin

# Register your models here.
from .models import tutorMeUser,Course,Schedule, ScheduleStudent, Appointment
admin.site.register(tutorMeUser)


class MyModelAdmin(admin.ModelAdmin):
    list_display =["Subject","course_name","course_number"]
admin.site.register(Course,MyModelAdmin)

class MySchedule(admin.ModelAdmin):
    list_display =["tutor","class_name"]
admin.site.register(Schedule,MySchedule)

class studentSchedule(admin.ModelAdmin):
    list_display =["student", "tutor","class_name"]
admin.site.register(ScheduleStudent,studentSchedule)

class AppointmentAdmin(admin.ModelAdmin):
    list_display =["student", "tutor","class_name"]
admin.site.register(Appointment,AppointmentAdmin)