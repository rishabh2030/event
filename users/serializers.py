from rest_framework import serializers
from .models import User
from datetime import datetime
from django.contrib.auth import authenticate
from helper import messages,keys

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'dob', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_dob(self, value):
        """
        Validate the date of birth format and range.
        """
        try:
            date_string = value.strftime("%Y-%m-%d")
            dob = datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            raise serializers.ValidationError(messages.INVALID_DATE_FORMAT)
        
        return dob

    def create(self, validated_data):
        """
        Create and return a new User instance.
        """
        user_obj = User.objects.create(
            email=validated_data[keys.EMAIL],
            name=validated_data[keys.NAME],
            dob=validated_data[keys.DOB]
        )
        user_obj.set_password(validated_data[keys.PASSWORD])
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, write_only=True, required=True)
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        """
        Validate the user's credentials.
        """
        email = attrs.get(keys.EMAIL)
        password = attrs.get(keys.PASSWORD)

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError(messages.UNABLE_TO_PROVIDE_ACESS_WITH_CREDENTIALS)
        else:
            raise serializers.ValidationError(messages.INVALID_INPUT)

        attrs[keys.USER] = user
        return attrs