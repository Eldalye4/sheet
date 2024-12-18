"""
URL configuration for library2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bookapp.views import retrievedepartments,deptdisplay , addnewdepartment,addnewbook
from Bookapp.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depall',retrievedepartments,name='list_all_departments'),
    path('department/<int:id>',deptdisplay ,name='display/department'),
    path('newdepartment',addnewdepartment,name='add_new_department'),
    path('department/<int:id>newbook',addnewbook ,name='add_new_book'),
    path('signup',signup,name='sign_up'),
]
