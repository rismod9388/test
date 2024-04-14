from django.shortcuts import render
from django.urls import path
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from . import views

# Create your views here.

def index(request):
    ##전달할 정보 없을시 {}로 표시
    return render(request,'homemain/index.html',{})

def boardList(request):
     return HttpResponse("Invalid request method", status=405)