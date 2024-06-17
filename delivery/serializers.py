from rest_framework import serializers
from .models import Boxpackage, Container, Package, Delivery
from crm.serializers import UsersSerializer
from .models import Users

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        # Изменим метод валидации, чтобы использовать вашу модель пользователя
        try:
            user = Users.objects.get(email=attrs['email'])
        except Users.DoesNotExist:
            raise serializers.ValidationError('No active account found with the given credentials')

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('No active account found with the given credentials')

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'email': user.email,
                'phone': user.phone,
            }
        }

class BoxpackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxpackage
        fields = ['location', 'post_index', 'description']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = ['id']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'