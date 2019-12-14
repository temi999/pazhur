from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('nodes/<int:pk>', views.NodeDetail.as_view()),
    path('reel_sets/', views.ReelSetList.as_view()),
    path('reels/<int:pk>/', views.ReelDetail.as_view()),
    path('reels/<int:pk>/', views.ReelDetail.as_view()),
    path('reel_sets/<int:pk>/', views.ReelSetDetail.as_view()),
    path('default_nodes/<int:pk>/', views.DefaultNodeDetail.as_view()),
    path('default_reels/<int:pk>/', views.DefaultReelDetail.as_view()),
    path('default_reel_sets/', views.DefaultReelSetList.as_view()),
    path('default_reel_sets/<int:pk>/', views.DefaultReelSetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('documentation', views.documentation, name='documentation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
