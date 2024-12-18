from django.db import models

# Create your models here.
class  department(models.Model):
    code=models.CharField(max_length=4)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.code
    
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    year=models.IntegerField()
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name