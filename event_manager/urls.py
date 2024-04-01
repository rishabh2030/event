from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('add-event/', EventListCreateAPIView.as_view(),name="add event"),
    path('events-op/<int:id>/', EventRetrieveUpdateDestroyAPIView.as_view(),name="add event"),
]