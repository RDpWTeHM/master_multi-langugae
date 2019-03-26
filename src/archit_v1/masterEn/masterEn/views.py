# masterEn/views.py
"""
"""

import os

from django.http import Http404
from django.shortcuts import render


def home(request):
    return render(request, 'page.html', {})


def contact(request):
    return render(request, 'contact.html', {})
