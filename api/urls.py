from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('reels/', views.ReelList.as_view()),
    path('reel_sets/', views.ReelSetList.as_view()),
    path('reels/<int:pk>/', views.ReelDetail.as_view()),
    path('reel_sets/<int:pk>/', views.ReelSetDetail.as_view()),
    path('default_reels/<int:pk>/', views.DefaultReelDetail.as_view()),
    path('default_reel_sets/', views.DefaultReelSetList.as_view()),
    path('default_reel_sets/<int:pk>/', views.DefaultReelSetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
