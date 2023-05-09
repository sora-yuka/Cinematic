from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from applications.accounts.serializers import UserSerializer

User = get_user_model()

class UserRegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        responce = super().post(request, *args, **kwargs)
        return Response('We have sent you an activation code to your email!')
    
    
class UserActivationApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'wrong code'}, status=status.HTTP_400_BAD_REQUEST)