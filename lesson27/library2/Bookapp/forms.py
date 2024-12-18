from django import forms

from .models import department,Book

class departmentform(forms.ModelForm):
    class Meta:
        model=department
        fields='__all__'
        

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        exclude=['dept']