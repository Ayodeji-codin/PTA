from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def  home(request): 
    return render(request,'home.html',{'user':request.user.username}) 

def student(request):
    evaluation = Evaluation.objects.filter(id_num=1)
    student = Student.objects.all()
    return render(request,'student.html',{
        'student':student,
        'eval':evaluation
    })























def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('login')

    return render(request,'signup.html',{
        'form':SignupForm()
    })
def login(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('home')
    return render(request,'login.html',{'form':LoginForm()})