from django.contrib import admin
from .models import *
# Register your models here.


class MusicsAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    ordering = ['id']


admin.site.register(Musics, MusicsAdmin)
