from django.urls import path
from . import views

urlpatterns = [
    path(r'get/random/', views.random_music, name='random_music'),
    path(r'get/<int:pk>/', views.get_music, name='get_music')
]