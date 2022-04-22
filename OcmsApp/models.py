from django.db import models

# Create your models here.

class Accounts(models.Model):
    AccountID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=300)
    Password = models.CharField(max_length=200)
    Type = models.CharField(max_length=1)

