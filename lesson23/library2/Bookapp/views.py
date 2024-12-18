from django.shortcuts import render
from .models import department

def retrievedepartments(request):
    s=department.objects.all()
    return render(request,'Bookapp/listdepatments.html',{'department':s})
