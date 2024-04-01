# views.py
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from event_manager.models import Event
from event_manager.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated

class EventSearchAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['title', 'description']

class EventFilterByDateAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = []
    
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            return Event.objects.filter(date__range=[start_date, end_date])
        return Event.objects.all()

class EventFilterByLocationAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['location']

class EventSortByDateAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [OrderingFilter]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['date']

class EventSortByTimeAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [OrderingFilter]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['time']