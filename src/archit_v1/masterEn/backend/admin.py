from django.contrib import admin

from .models import Dict


@admin.register(Dict)
class DictAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'result', 'times', 'add_date')
    list_per_page = 100
