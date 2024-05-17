from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UsersSerializer
from .models import Users
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken





class Register(APIView):

    def post(self, request):

        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        users = serializer.save()

        access_token = AccessToken.for_user(users)
        refresh_token = RefreshToken.for_user(users)


        return Response({
            'access_token': str(access_token),
            'refresh_token': str(refresh_token)
        })


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        users = Users.objects.filter(email= email).first()

        if users is None:
            raise AuthenticationFailed('User not found')
        
        if not check_password(password, users.password):
            raise AuthenticationFailed('Incorect password')
        
        access_token = AccessToken.for_user(users)
        refresh_token = RefreshToken.for_user(users)

        
        return Response({
            'access_token': str(access_token),
            'refresh_token': str(refresh_token)
        })

        


