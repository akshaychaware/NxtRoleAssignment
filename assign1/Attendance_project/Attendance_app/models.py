from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    roll_no=models.IntegerField()
    student_class=models.CharField(max_length=30)
    email=models.EmailField(unique=True, max_length=254)