# backend/views.py
"""

TODO:
  - move recently/mostly 5 translations to a single backend.
"""

from django.shortcuts import render

import sys
from django.contrib.auth.decorators import login_required

from django.shortcuts import Http404
from django.http.response import JsonResponse
# import json

from masterencore.fanyiapi import baidu as fanyiapi

from .models import Dict


@login_required(login_url='/accounts/login/')
def index(request):
    # ...

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # TODO: currently, recently 5 translates; update to mostly 5 translate.
    dicts = Dict.objects.all()

    context = {
        'num_visits': num_visits,
        'most5trans': dicts[len(dicts) - 5:],
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'backend/index.html', context=context)


@login_required(login_url='/accounts/login/')
def translate(request):
    if request.method == "POST":
        # search current database:
        '''TODO:
            - should Case-insensitive
            - participle ?
        '''
        word = request.POST['translate']
        # print(request.POST["translate"], file=sys.stderr)
        result = None
        try:
            obj = Dict.objects.get(word=word)
            result = obj.result

            obj.times += 1
            obj.save()
        except Dict.DoesNotExist:  # new query
            # third-part API
            api_resp = fanyiapi.fanyi(word)
            result = api_resp['trans_result'][0]['dst']

            Dict.objects.create(word=word, result=result, times=1)

        # response
        return JsonResponse({'ret': result})
    else:
        raise Http404("wrong request method.")
