from django import forms

from .models import department

class departmentform(forms.ModelForm):
    class Meta:
        model=department
        fields='__all__'