from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    pass
    return render(request,'index.html')

def survey(request):
    return render(request, 'survey.html')

def login(request):
    pass
    return render(request,'login.html')

def register(request):
    pass
    return render(request,'register.html')

def logout(request):
    pass
    return redirect('/index/')