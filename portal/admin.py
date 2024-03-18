from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import Contact
from.models import Event
from.models import View
from.models import Signup
from.models import Login,Application,Registration
# from portal.models import Course_Registration
# from.models import Courses



# from django.contrib.auth.models import Group,User
admin.site.site_header='Welcome to School portal'


# Register your models here.
# admin.site.unregister(Group)
# admin.site.unregister(User)


class ContactAdmin(admin.ModelAdmin):
    list_display=['id','title','mobile','mail']

class EventAdmin(admin.ModelAdmin):
    list_display=['id','img','title','desc']

class ViewAdmin(admin.ModelAdmin):
    list_display=['id','img','title']

class SignupAdmin(admin.ModelAdmin):
    list_display=['id','username','email','password']

class RegistrationAdmin(admin.ModelAdmin):
    list_display=['id','course_code','course_title','credit_unit',
                  'id','course_code1','course_title1','credit_unit1',
                  'id','course_code2','course_title2','credit_unit2',
                  'id','course_code3','course_title3','credit_unit3',
                  'id','course_code4','course_title4','credit_unit4',
                  'id','course_code5','course_title5','credit_unit5',
                  'id','course_code6','course_title6','credit_unit6',
                  'id','course_code001','course_title001','credit_unit001',
                  'id','course_code002','course_title002','credit_unit002',
                  'id','course_code003','course_title003','credit_unit003',
                  'id','course_code004','course_title004','credit_unit004',
                  'id','course_code005','course_title005','credit_unit005',
                  'id','course_code006','course_title006','credit_unit006',
                  'id','course_code007','course_title007','credit_unit007',
                  ]
class LoginAdmin(admin.ModelAdmin):
    list_display=['id','Username', 'password']

class ApplicationAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','gender','email','phonenumber','course','nationality','state','lg']



admin.site.register(Contact,ContactAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(View,ViewAdmin)
admin.site.register(Signup,SignupAdmin)
admin.site.register(Login,LoginAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Application,ApplicationAdmin)


