from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from markdown import markdown
from .models import PinPost, Post
from markdown_newtab import NewTabExtension


def hide_page(request):
    pin_msg_list = PinPost.objects.all().order_by('-pin', '-create_date')
    msg_list = Post.objects.all().order_by('-create_date')
    md_ex = [NewTabExtension(),
             'pymdownx.inlinehilite',
             'pymdownx.highlight',
             'pymdownx.inlinehilite',
             'pymdownx.extrarawhtml',
             'pymdownx.tilde']

    for msg in pin_msg_list:
        msg.main_text = markdown(msg.main_text, )
    for msg in msg_list:
        msg.main_text = markdown(msg.main_text)
    return render(request, 'hidepage.html', context={'pin_msg_list': pin_msg_list,
                                                     'msg_list': msg_list})

