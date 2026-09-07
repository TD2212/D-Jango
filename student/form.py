from django import forms
from .models import Student,Course,Department

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"



class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"

class Department(forms.ModelChoiceField):
    class Meta:
        model=Department
        fields="__all__"