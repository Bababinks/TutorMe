from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['tutor', 'class_name', 'input_rate', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                  'saturday', 'sunday']


class BugReportForm(forms.Form):
    bug_description = forms.CharField(label="enter any issues you may encounter", widget=forms.Textarea)
