from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('applicants',views.applicants, name='applicants'),
    path('registration',views.registration, name='registration')
]