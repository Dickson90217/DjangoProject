from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
# Create your views here.
def hello(request):
    text = "<h1>welcome to howard!</h1>"
    return HttpResponse(text)

def login(request):
    return render(request, 'loginTemolates.html')
#忘記密碼
def loginfg(request):
    fg = request.POST.get('loginfg')
    return HttpResponse('no')
#註冊
def loginus(request):
    us = request.POST.get('loginus')
    return HttpResponse('hi')
#登出
def logout(request):
    return HttpResponse('LOGOUT success')



#選擇
def kind(request):
    return render(request, 'animal.html')
def animals(request):
    animal = request.POST.get('animal')
    if animal == 'dog':
        return render(request, 'dogs.html')
    elif animal == 'cat':
        return render(request, 'cats.html')
    elif animal == 'other':
        return render(request, 'others.html')
    else:
        return HttpResponse('fail')
def catts(request):
    return HttpResponse('cat')
def others(request):
    return HttpResponse('pig')
def dogproject(request):
        return render(request,'dogsouse.html')

