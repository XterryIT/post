from rest_framework import serializers
from .models import User


# new code 

# Conversion lines to json format lines
class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)





# old code

# class UserSerializer(serializers.ModelSerializer):
#     class Meta(object):
#         model = User
#         fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password']