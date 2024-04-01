from rest_framework import generics,status
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from helper.functions import HttpStatusCode,ResponseHandling
from rest_framework.permissions import IsAuthenticated
from helper import messages

class EventListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            user = request.user
            request.data['user'] = user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS,serializer.data),status=HttpStatusCode.HTTP_201_CREATED)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(messages.OPERATION_FAILED,e),status=HttpStatusCode.HTTP_400_BAD_REQUEST)

class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'  

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS,serializer.data),status=HttpStatusCode.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        user = request.user
        request.data['user'] = user.id

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS,serializer.data),status=HttpStatusCode.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS,messages.DELTED_SUCCESS),status=HttpStatusCode.HTTP_202_ACCEPTED)

