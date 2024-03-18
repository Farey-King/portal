from django.db import models
from datetime import datetime,timezone
# from django.contrib.auth.models import AbstractUser

# Create your models here
class Contact(models.Model):
    title=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Event(models.Model):
    img=models.ImageField(upload_to="media")
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    def __str__(self):
        return self.title
    
class View(models.Model):
    img=models.ImageField(upload_to="media")
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Signup(models.Model):
    # full_name=models.CharField(max_length=100, blank=True,null=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    # phone_number=models.CharField(max_length=100, blank=True,null=True)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
    
class Login(models.Model):
    
    Username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.Username 
    
class Registration(models.Model):
    # rid=models.IntegerField
    course_code=models.CharField(max_length=100)
    course_title=models.CharField(max_length=100)
    credit_unit=models.CharField(max_length=100)
    course_code1=models.CharField(max_length=100)
    course_title1=models.CharField(max_length=100)
    credit_unit1=models.CharField(max_length=100)
    course_code2=models.CharField(max_length=100)
    course_title2=models.CharField(max_length=100)
    credit_unit2=models.CharField(max_length=100)
    course_code3=models.CharField(max_length=100)
    course_title3=models.CharField(max_length=100)
    credit_unit3=models.CharField(max_length=100)
    course_code4=models.CharField(max_length=100)
    course_title4=models.CharField(max_length=100)
    credit_unit4=models.CharField(max_length=100)
    course_code5=models.CharField(max_length=100)
    course_title5=models.CharField(max_length=100)
    credit_unit5=models.CharField(max_length=100)
    course_code6=models.CharField(max_length=100)
    course_title6=models.CharField(max_length=100)
    credit_unit6=models.CharField(max_length=100)
    course_code001=models.CharField(max_length=100)
    course_title001=models.CharField(max_length=100)
    credit_unit001=models.CharField(max_length=100)
    course_code002=models.CharField(max_length=100)
    course_title002=models.CharField(max_length=100)
    credit_unit002=models.CharField(max_length=100)
    course_code003=models.CharField(max_length=100)
    course_title003=models.CharField(max_length=100)
    credit_unit003=models.CharField(max_length=100)
    course_code004=models.CharField(max_length=100)
    course_title004=models.CharField(max_length=100)
    credit_unit004=models.CharField(max_length=100)
    course_code005=models.CharField(max_length=100)
    course_title005=models.CharField(max_length=100)
    credit_unit005=models.CharField(max_length=100)
    course_code006=models.CharField(max_length=100)
    course_title006=models.CharField(max_length=100)
    credit_unit006=models.CharField(max_length=100)
    course_code007=models.CharField(max_length=100)
    course_title007=models.CharField(max_length=100)
    credit_unit007=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.course_code},{self.course_title},{self.credit_unit}'

class Application(models.Model):
    aid=models.ImageField
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    lg=models.CharField(max_length=100)
    def __str__(self):
        return self.fname
    
    



    