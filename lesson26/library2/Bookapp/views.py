from django.shortcuts import render
from django.http import HttpResponse
from .models import department
from .forms import departmentform
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