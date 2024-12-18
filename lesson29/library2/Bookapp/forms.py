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
        

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Mysignupform(UserCreationForm):
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')