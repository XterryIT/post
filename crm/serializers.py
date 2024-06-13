from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users

# Conversion lines to json format lines
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'email', 'password', 'is_register']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_register': {'default': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_register = True
        if password is not None:
            instance.password = make_password(password)
        instance.save()
        return instance



