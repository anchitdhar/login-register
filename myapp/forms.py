from myapp.models import *
from django import forms

class Employee(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"