from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework import serializers, status



class UserApiView(APIView):
    # def get(self, request):
    #     u = User.objects.all()

    #     return Response({'users': UserSerializer(u, many=True)})
    

 def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
























# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, email=request.data['email'])
    
#     if user.password != request.data['password']:
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
    
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(instance=user)
#     return Response({"token": token.key, "user": serializer.data})

# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
#         user = User.objects.get(email=request.data['email'])
#         user.password = request.data['password']  # Assigning the password
#         user.save()
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key, "user": serializer.data})
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def test_token(request):
#     return Response({})


