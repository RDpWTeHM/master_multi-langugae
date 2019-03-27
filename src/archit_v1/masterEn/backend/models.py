# backend/models.py
"""
"""

from django.db import models


class Dict(models.Model):
    add_date = models.DateField(auto_now=True)
    word = models.CharField(max_length=128)
    result = models.CharField(max_length=128)

    times = models.IntegerField()

    def __str__(self):
        string = '[{}] {word}->{result}; {times} times'.format(
            id(self), **dict(self.__dict__))
        return string
