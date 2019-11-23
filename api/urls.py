from django.urls import path

from .views import SlotSetsView, CreateSlotSetView, UpdateSlotSetView

urlpatterns = [
    path('list/', SlotSetsView.as_view()),
    path('create/', CreateSlotSetView.as_view()),
    path('update/<int:pk>', UpdateSlotSetView.as_view()),
]