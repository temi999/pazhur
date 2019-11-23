from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reel_sets/', views.reel_sets, name='reel_sets'),
]