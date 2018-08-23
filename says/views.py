# Create your views here.

from .models import PeopleSays
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.forms.models import model_to_dict

says_pre_page = 5


def get_says_page(request, pg):
    context = {}
    sl = PeopleSays.objects.all()
    end = (len(sl)-1)/says_pre_page
    sl = sl[says_pre_page*(pg-1):says_pre_page*pg]
    says_list = []
    for l in sl:
        u = {}
        s = model_to_dict(l)
        for k in ['name', 'url', 'text']:
            u[k] = s[k]
        u['time'] = l.time
        says_list.append(u)
    if len(says_list) > 0:
        context['says_list'] = says_list
    else:
        context['err'] = '这里啥都没有'
    says_pg = {
        'current': pg,
        'before': range(1, pg)
    }
    if pg > 1:
        says_pg['pre'] = pg-1
    if pg < end:
        says_pg['next'] = pg + 1
    context['says_pg'] = says_pg
    return render(request, 'get_says.html', context)


def put_says(request):
    if request.method == 'POST':
        dct = request.POST
        op = PeopleSays()
        op.url = dct['url']
        op.name = dct['name']
        op.text = dct['say_text']
        op.save()

