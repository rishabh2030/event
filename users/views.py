from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from helper import messages,functions
from .serializers import UserRegisterSerializer, UserLoginSerializer
from helper.functions import UserMethods, JWTTMethods, ResponseHandling, HttpStatusCode
class UserRegisterAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    """
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseHandling.success_response_message(messages.REGISTRACTION_USER,JWTTMethods.token_as_dictionary(UserMethods.get_user(email=request.data.get('email')))),status=HttpStatusCode.HTTP_201_CREATED)
        return Response(ResponseHandling.failure_response_message(messages.OPERATION_FAILED,serializer.errors),status=HttpStatusCode.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(generics.CreateAPIView):
    """
    API endpoint for user login.
    """
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(ResponseHandling.success_response_message(messages.LOGIN_SUCCESS,JWTTMethods.token_as_dictionary(UserMethods.get_user(email=request.data.get('email')))),status=HttpStatusCode.HTTP_201_CREATED)
        return Response(ResponseHandling.failure_response_message(messages.OPERATION_FAILED,serializer.errors),status=HttpStatusCode.HTTP_400_BAD_REQUEST)
