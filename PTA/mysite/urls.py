from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name = 'login'),
    path('home',views.home, name='home'),
    path('signup',views.signup, name ='signup'),
    path('student',views.student,name = 'student')
]                                                               