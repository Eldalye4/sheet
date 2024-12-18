from django.shortcuts import render
from .models import department

def retrievedepartments(request):
    s=department.objects.all()
    return render(request,'Bookapp/listdepatments.html',{'department':s})

def deptdisplay(request ,id):
    dept=department.objects.get(pk=id)
    return render(request,"Bookapp/department.html",{'department':dept})