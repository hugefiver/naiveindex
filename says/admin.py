from django.contrib import admin
from .models import PeopleSays

# Register your models here.


class PeopleSaysAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'text']
    ordering = ['-time']


admin.site.register(PeopleSays, PeopleSaysAdmin)
