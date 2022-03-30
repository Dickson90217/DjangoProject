
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('howard/', views.howard),
    path('login/', views.login),
    path('loginfg/', views.loginfg),
    path('loginus/', views.loginus),
    path('logout/', views.logout),
    path('logoutssd/', views.logoutssd),
    path('loginussue/', views.loginussue),
    path('loginfgssue/', views.loginfgssue),
    path('backtofirst/', views.backtofirst),
    path('kind/', views.kind),
    path('adopt/', views.adopt),
    path('adoptfor/', views.adoptfor),
    path('adoprrfor/', views.adoprrfor),
    path('whatadopt/', views.whatadopt),
    path('loginin/', views.loginin),
    path('animals/', views.animals),
    path('logafter/', views.logafter),
    path('help/', views.help),
    path('helpfor/', views.helpfor),
    path('helppfor/', views.helppfor)
    ]
