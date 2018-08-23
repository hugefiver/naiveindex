from django.shortcuts import render, get_object_or_404
from .models import Musics
import random

# Create your views here.


def random_music(request):
    count = Musics.objects.count()
    if count:
        pk = random.randrange(count)
    else:
        pk = -1
    return get_music(request, pk=pk)


def get_music(request, pk):
    if pk < 0:
        return render(request, 'music.html')
    music = Musics.objects.all()[pk]
    return render(request, 'music.html', {'music': music})

