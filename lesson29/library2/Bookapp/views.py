from django.shortcuts import render
from django.http import HttpResponse
from .models import department
from .forms import departmentform,Bookform
from django.shortcuts import redirect

def retrievedepartments(request):
    s=department.objects.all()
    return render(request,'Bookapp/listdepatments.html',{'department':s})

def deptdisplay(request ,id):
    dept=department.objects.get(pk=id)
    return render(request,"Bookapp/department.html",{'department':dept})


def addnewdepartment(request):
    
    form=departmentform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_departments')
    return render(request,"Bookapp/newdepartment.html",{'form':form})


def addnewbook(request ,id):
    dept=department.objects.get(pk=id)
    

    form=Bookform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form=form.save(commit=False)
        form.dept=dept
        form.save()
        return redirect('display/department',id=dept.pk)



    return render(request,"Bookapp/addnewbook.html",{'department':dept,'form':form})

from django.contrib.auth.forms import UserCreationForm
from .forms import Mysignupform
from django.contrib.auth import login
def signup(request):
    
    form=Mysignupform(request.POST or None,request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('list_all_departments')
    return render(request,"Bookapp/sign.html",{'form':form})
