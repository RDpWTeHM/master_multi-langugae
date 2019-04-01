# backend/views.py
"""

TODO:
  -[x] done: move recently/mostly 5 translations to a single backend.
"""

from django.shortcuts import render

import sys
from django.contrib.auth.decorators import login_required

# from django.http.response import HttpResponse
from django.shortcuts import Http404
from django.http.response import JsonResponse
# import json

from masterencore.fanyiapi import baidu as fanyiapi

from .models import Dict

from .utils import get_recently_trans_orm, get_mostly_trans_orm


@login_required(login_url='/accounts/login/')
def index(request):
    # ...

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'backend/index.html',
                  context={'num_visits': num_visits, })


@login_required(login_url='/accounts/login/')
def recommender(request):
    whatly = request.GET.get('whatly')
    if whatly:
        # exec('func = get_' + whatly + '_trans_orm') work too
        func = eval("get_" + whatly + "_trans_orm")
        qs = func(5)
        return JsonResponse({
            whatly: [{k: str(v) for k, v in obj.__dict__.items()}
                     for obj in qs],
        })

    else:
        recently5ORMDict = get_recently_trans_orm(5)
        mostly5ORMDict = get_mostly_trans_orm(5)
        mostly = [{k: str(v) for k, v in obj.__dict__.items()}
                  for obj in mostly5ORMDict]
        recently = [{k: str(v) for k, v in obj.__dict__.items()}
                    for obj in recently5ORMDict]
        return JsonResponse({
            'recently': recently,
            'mostly': mostly})


@login_required(login_url='/accounts/login/')
def translate(request):
    if request.method == "POST":
        # search current database:
        '''TODO:
            -[o] should Case-insensitive
            -[o] blank begin/end strip
            -[o] participle ?
        '''
        whichDirection = request.POST.get("whichDirection")
        word = request.POST['translate']
        # print(request.POST["translate"], file=sys.stderr)
        result = None

        if whichDirection == "En2Zh":
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

        elif whichDirection == "Zh2En":
            api_resp = fanyiapi.enwrite(word)
            result = api_resp['trans_result'][0]['dst']

        # response
        return JsonResponse({'ret': result})
    else:
        # TODO: upate 40x by HTTP spec
        raise Http404("wrong request method.")
