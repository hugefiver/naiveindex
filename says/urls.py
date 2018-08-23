from django.urls import path
from .views import *

app_name = 'says'
urlpatterns = [
    path(r'says/page/<int:pg>/', get_says_page, name='re_page'),
    path(r'says/add/', put_says, name='send')
]