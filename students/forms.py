from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['name', 'teacher', 'student']


class MessageForm(forms.Form):
    student_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)