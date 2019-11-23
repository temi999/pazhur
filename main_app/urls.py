from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slot_sets/', views.slot_sets, name='slot_sets'),
]