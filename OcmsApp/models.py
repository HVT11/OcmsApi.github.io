from datetime import date
from django.db import models
from psycopg2 import Date

# Create your models here.

class Accounts(models.Model):
    AccountID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=300)
    Password = models.CharField(max_length=200)
    Type = models.CharField(max_length=1)
    DateCreate = models.DateField(auto_now=True)

class Teachers(models.Model):
    TeacherID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500, null=True)
    Email = models.CharField(max_length=300, null=True)
    Phone = models.CharField(max_length=300, null=True)
    Avatar = models.CharField(max_length=300, null=True)
    Username = models.CharField(max_length=300)

class Students(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500, null=True)
    Gentle = models.CharField(max_length=1)
    StudentCode = models.CharField(max_length=300, null=True)
    DateOfBirth = models.DateField(null = True)
    Email = models.CharField(max_length=300, null=True)
    Avatar = models.CharField(max_length=300, null=True)
    Username = models.CharField(max_length=300)
    ClassID = models.IntegerField()

class Classes(models.Model):
    ClassID = models.AutoField(primary_key=True)
    ClassCode = models.CharField(max_length=300,null=True)
    ClassName = models.CharField(max_length=500, null=True)
    Schedule = models.CharField(max_length=300, null=True)
    TotalStu = models.CharField(max_length=300, null=True)
    DateCreate = models.DateField(auto_now=True)
    TeacherID = models.IntegerField()
    
