from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users
import jwt, datetime

# new code 

# Conversion lines to json format lines
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = make_password(password)
        instance.save()
        return instance



