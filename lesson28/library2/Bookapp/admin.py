from django.contrib import admin

# Register your models here.
from .models import department,Book
admin.site.register((department,Book))