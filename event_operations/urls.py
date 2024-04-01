from django.urls import path
from .views import *

urlpatterns = [
    path('events/search/', EventSearchAPIView.as_view(), name='event-search'),
    path('events/filter_by_date/', EventFilterByDateAPIView.as_view(), name='event-filter-by-date'),
    path('events/filter_by_location/', EventFilterByLocationAPIView.as_view(), name='event-filter-by-location'),
    path('events/sort_by_date/', EventSortByDateAPIView.as_view(), name='event-sort-by-date'),
]
