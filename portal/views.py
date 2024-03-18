from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError



# Create your views here.
from django.contrib.sessions.models import Session
from .models import Contact
from .models import Event
from .models import View
from .models import Signup
from .models import Login
from .models import Application,Registration
# from .models import Courses



def index(request):
    Contacts =Contact.objects.all()
    Events =Event.objects.all()
    Views =View.objects.all()
    return render(request,'index.html',{"Contacts":Contacts,"Events":Events,"Views":Views})

def signup(request):
    if request.method == 'POST':
            # full_name = request.POST['full_name']
            Username = request.POST['username']
            email = request.POST['email']
            # phonenumber = request.POST['phonenumber']
            password = request.POST['password']
            user = Signup.objects.create(username=Username,email=email,password=password)
            user.save();
            return redirect('login')
    else:
         return render(request,'signup.html')
         

  


def login(request):
    if request.method=='POST':
         
        Username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=Username, password=password)
        if user is not None:
          print(user,'--------')
          login(request, user)
        return redirect('registration')
        # Redirect to a success page.
        ...
    else:
     
        return render(request, "login.html")
        # Return an 'invalid login' error message.
        ...  

# def login(request):
#       if  request.method == 'POST':
#             username = request.POST.get('username')
#           #   print(username)
#             password = request.POST.get('password')
#           #   print(password)
#             user = authenticate(request,username=username,password=password)

#             if user is not None:
#                  print(user.username)
#                  login(request,user)

#             return redirect('registration')
            
#       else:
#         return render(request, "login.html")
          #   messages.info(request,'Please register before login')

             

          #   return render(request,"signup.html")
      
      

def registration(request):
            if request.method=='POST':
                course_code = request.POST.get('course_code')
                course_title = request.POST.get('course_title')
                credit_unit = request.POST.get('credit_unit')
                course_code1 = request.POST.get('course_code1')
                course_title1 = request.POST.get('course_title1')
                credit_unit1 = request.POST.get('credit_unit1')
                course_code2 = request.POST.get('course_code2')
                course_title2 = request.POST.get('course_title2')
                credit_unit2 = request.POST.get('credit_unit2')
                course_code3 = request.POST.get('course_code3')
                course_title3 = request.POST.get('course_title3')
                credit_unit3= request.POST.get('credit_unit3')
                course_code4 = request.POST.get('course_code4')
                course_title4 = request.POST.get('course_title4')
                credit_unit4= request.POST.get('credit_unit4')
                course_code5 = request.POST.get('course_code5')
                course_title5 = request.POST.get('course_title5')
                credit_unit5=request.POST.get('credit_unit5')
                course_code6 = request.POST.get('course_code6')
                course_title6 = request.POST.get('course_title6')
                credit_unit6=request.POST.get('credit_unit6')
                course_code001=request.POST.get('course_code001')
                course_title001=request.POST.get('course_title001')
                credit_unit001=request.POST.get('credit_unit001')
                course_code002=request.POST.get('course_code002')
                course_title002=request.POST.get('course_title002')
                credit_unit002=request.POST.get('credit_unit002')
                course_code003=request.POST.get('course_code003')
                course_title003=request.POST.get('course_title003')
                credit_unit003=request.POST.get('credit_unit003')
                course_code004=request.POST.get('course_code004')
                course_title004=request.POST.get('course_title004')
                credit_unit004=request.POST.get('credit_unit004')
                course_code005=request.POST.get('course_code005')
                course_title005=request.POST.get('course_title005')
                credit_unit005=request.POST.get('credit_unit005')
                course_code006=request.POST.get('course_code006')
                course_title006=request.POST.get('course_title006')
                credit_unit006=request.POST.get('credit_unit006')
                course_code007=request.POST.get('course_code007')
                course_title007=request.POST.get('course_title007')
                credit_unit007=request.POST.get('credit_unit007')

    # try:

                user = Registration.objects.create(course_code=course_code, course_title=course_title, credit_unit=credit_unit, course_code1=course_code1, course_title1=course_title1, credit_unit1=credit_unit1, course_code2=course_code2, course_title2=course_title2, credit_unit2=credit_unit2, course_code3=course_code3, course_title3=course_title3, credit_unit3=credit_unit3, course_code4=course_code4, course_title4=course_title4, credit_unit4=credit_unit4,course_code5=course_code5, course_title5=course_title5, credit_unit5=credit_unit5,course_code6=course_code6, course_title6=course_title6, credit_unit6=credit_unit6,course_code001=course_code001, course_title001=course_title001, credit_unit001=credit_unit001,course_code002=course_code002, course_title002=course_title002, credit_unit002=credit_unit002, course_code003=course_code003, course_title003=course_title003, credit_unit003=credit_unit003,course_code004=course_code004, course_title004=course_title004, credit_unit004=credit_unit004,course_code005=course_code005, course_title005=course_title005, credit_unit005=credit_unit005,course_code006=course_code006, course_title006=course_title006, credit_unit006=credit_unit006,course_code007=course_code007, course_title007=course_title007, credit_unit007=credit_unit007)
                user.save()
                return redirect('index')
            return render(request,'registration.html')
            
    # except IntegrityError as e:
    #      print(f"IntegrityError occurred: {e}")
    # except Exception as e:
    #      print(f"another error occurred: {e}")
         
    # #         print("course inserted successfully")
    

            

            
            
	

def logout(request):
	logout(request)
	return redirect ('home')

    

def applicants(request):
    if request.method =='POST':
         fname = request.POST.get('fname')
         lname = request.POST.get('lname')
         gender = request.POST.get('gender')
         email = request.POST.get('email')
         phonenumber = request.POST.get('phonenumber')
         course = request.POST.get('course')
         nationality = request.POST.get('nationality')
         state = request.POST.get('state')
         lg = request.POST.get('lg')
         user=Application.objects.create(fname=fname,lname=lname,gender=gender,email=email,phonenumber=phonenumber,course=course,nationality=nationality,state=state,lg=lg)
         user.save
         return redirect('index')

         
    return render(request,'applicants.html')






