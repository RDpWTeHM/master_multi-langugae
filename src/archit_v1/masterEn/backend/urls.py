""" masterEn/backend/urls.py
"""

from django.urls import path
# from django.http import HttpResponse
from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.index, name="index"),
    path('recommender/', views.recommender, name='recommender'),

    path("translate/", views.translate, name="translate"),
]
