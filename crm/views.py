from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UsersSerializer
from .models import Users
from django.contrib.auth.hashers import check_password
from datetime import timezone
import jwt, datetime




class Register(APIView):

    def post(self, request):

        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        users = Users.objects.filter(email= email).first()

        if users is None:
            raise AuthenticationFailed('User not found')
        
        if not check_password(password, users.password):
            raise AuthenticationFailed('Incorect password')

        
        return Response({'message': 'success'})

        


