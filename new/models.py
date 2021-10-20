from django.db import models




class LoginPage(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=8)
class Register(models.Model):
    Username=models.CharField(max_length=100)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Phone_number=models.IntegerField()
    Password=models.CharField(max_length=8)
class email(models.Model):
    email_id=models.EmailField(max_length=100)
    

    
    