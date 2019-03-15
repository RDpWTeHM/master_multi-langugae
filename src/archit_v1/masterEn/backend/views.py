from django.shortcuts import render

# Create your views here.

import sys
from django.contrib.auth.decorators import login_required

from django.shortcuts import Http404
from django.http.response import JsonResponse
# import json

from masterencore.fanyiapi import baidu as fanyiapi


@login_required(login_url='/accounts/login/')
def index(request):
    # ...

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'backend/index.html', context=context)


@login_required(login_url='/accounts/login/')
def translate(request):
    if request.method == "POST":
        # print(request.POST["translate"], file=sys.stderr)
        word = request.POST['translate']
        api_resp = fanyiapi.fanyi(word)
        return JsonResponse({'ret': api_resp['trans_result'][0]['dst']})
    else:
        raise Http404("wrong request method.")
