from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'email', 'password', 'is_register']
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
    
    

class UserDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['phone', 'email']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if not instance.first_name or not instance.last_name:
    #         representation['first_name'] = instance.email
    #         representation['last_name'] = instance.phone
    #     return representation


