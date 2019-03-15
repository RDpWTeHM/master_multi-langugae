"""masterEn/account_ext/urls.py
"""

from django.urls import path

# from django.http import HttpResponse
from django.shortcuts import render

from . import views


app_name = 'account_ext'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('register/done/',
         lambda request: render(request, 'account_ext/register_done.html', {}))
]
