"""masterEn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: HttpResponse('<h1>Welcome to Master English!</h1>')),

    path(r'favicon.ico',
         RedirectView.as_view(url=r'/static/favicon.ico')),

    path('backend/', include('backend.urls')),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

    path('account_ext/', include('account_ext.urls')),
]
