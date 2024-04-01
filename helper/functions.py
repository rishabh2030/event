from users.models import User
from rest_framework import status
import uuid

# Define HTTP Status Codes
class HttpStatusCode:
    HTTP_200_OK = status.HTTP_200_OK
    HTTP_201_CREATED = status.HTTP_201_CREATED
    HTTP_202_ACCEPTED = status.HTTP_202_ACCEPTED
    HTTP_204_NO_CONTENT = status.HTTP_204_NO_CONTENT
    HTTP_400_BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    HTTP_403_FORBIDDEN = status.HTTP_403_FORBIDDEN
    HTTP_404_NOT_FOUND = status.HTTP_404_NOT_FOUND
    HTTP_500_INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR

# Class of users operations
class UserMethods:
    """
    Class containing methods related to user operations.
    """
    @staticmethod
    def get_user(email):
        """
        Retrieve a user by email address.

        Args:
            email (str): Email address of the user to retrieve.

        Returns:
            User: User object if found.

        Raises:
            ValueError: If user with the given email does not exist.
        """
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            raise ValueError("User does not exist")

# Response handling
class ResponseHandling:
    """
    Class containing methods for handling API responses.
    """

    @staticmethod
    def failure_response_message(detail, result):
        """
        Generate an error response message.

        Args:
            detail (str): Message to provide additional details about the error.
            result (str): Message or result to include in the response.

        Returns:
            dict: Dictionary containing the error response details.
        """
        return {'detail': detail, 'result': result}

    @staticmethod
    def success_response_message(detail, result):
        """
        Generate a success response message.

        Args:
            detail (str): Message to provide additional details about the success.
            result (str): Message or result to include in the response.

        Returns:
            dict: Dictionary containing the success response details.
        """
        return {'detail': detail, 'result': result}
    
    @staticmethod
    def error_message_function(errors):
        """
        Generate error message when serializer is not valid.

        Args:
            errors (dict): Dictionary containing error messages.

        Returns:
            str: Concatenated error message.
        """
        for key, values in errors.items():
            error = [value[:] for value in values]
            err = ' '.join(map(str, error))
            return err

# Jwt Methods
class JWTTMethods:
    """
    Class containing methods for handling JWT tokens.
    """
    @staticmethod
    def token_as_dictionary(user):
        """
        Generate a dictionary response containing the access token and refresh token.

        Args:
            token (tuple): Tuple containing the access token and refresh token.

        Returns:
            dict: Dictionary containing the access token and refresh token.
        """
        token, refresh_token = user.get_tokens()
        return {"access_token": token, "refresh_token": refresh_token}