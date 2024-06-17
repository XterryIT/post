from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Boxpackage, Container, Package, Delivery
from .serializers import PackageSerializer, DeliverySerializer, BoxpackageSerializer
from crm.serializers import UserDeliverySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import random
from datetime import datetime, timedelta

class DeliveryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Извлечение аутентифицированного пользователя из токена
        user = request.user
        data = request.data
        email = data.get('to_user_email')
        phone = data.get('to_user_phone')
        size_package = data.get('size_package')
        fk_from_boxpackage = data.get('from_boxpackage')
        fk_to_boxpackage = data.get('to_boxpackage')

        # Проверка и создание пользователя получателя
        to_user, created = Users.objects.get_or_create(email=email, defaults={
            'phone': phone,
            'is_register': False
        })

        # Проверка наличия свободного контейнера
        container = Container.objects.filter(capacity=size_package, available=True).first()
        if not container:
            return Response({"error": "Нет доступного контейнера с требуемой вместимостью"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Создание посылки
        package = Package.objects.create(
            pin=random.randint(100, 999),
            required_capacity=size_package,
            status='In process',
            container=container
        )
        container.available = False
        container.save()

        # Создание записи доставки
        delivery = Delivery.objects.create(
            fk_package=package,
            fk_from_boxpackage=Boxpackage.objects.get(id=fk_from_boxpackage),
            fk_to_boxpackage=Boxpackage.objects.get(id=fk_to_boxpackage),
            departure_date=datetime.now(),
            arrival_date=datetime.now() + timedelta(days=2),
            from_user=user,  # Используем пользователя из токена
            to_user_phone=to_user.phone,
            to_user_email=to_user.email,
            size_package=size_package  # Сохраняем size_package
        )

        delivery_serializer = DeliverySerializer(delivery)
        user_serializer = UserDeliverySerializer(to_user)
        package_serializer = PackageSerializer(package)
        from_boxpackage_serializer = BoxpackageSerializer(Boxpackage.objects.get(id=fk_from_boxpackage))
        to_boxpackage_serializer = BoxpackageSerializer(Boxpackage.objects.get(id=fk_to_boxpackage))

        response_data = {
            'delivery': delivery_serializer.data,
            'user': user_serializer.data,
            'from_boxpackage': from_boxpackage_serializer.data,
            'to_boxpackage': to_boxpackage_serializer.data,
            'package': package_serializer.data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)