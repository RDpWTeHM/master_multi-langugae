# backend/utils.py

"""
"""

from .models import Dict


def get_recently_trans_orm(num):
    '''add middleware to multiplex
       - It may be abuse.
         But consider this function can used for CLI too!
         Not only the 'view'
    '''
    dicts = Dict.objects.all()
    return dicts[len(dicts) - num:]


def get_mostly_trans_orm(num):
    dicts = Dict.objects.all().order_by('times')
    return dicts.reverse()[:5]
