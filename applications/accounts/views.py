import logging
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from applications.accounts.serializers import ForgotPasswordFinishSerializer, ForgotPasswordSerializer, UserSerializer, ChangePasswordSerializer

User = get_user_model()
logger = logging.getLogger('main')


class UserRegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        logger.info('User has registrated!')
        responce = super().post(request, *args, **kwargs)
        return Response('We have sent you an activation code to your email!')
    
    
class UserActivationApiView(APIView):
    def get(self, request, activation_code):
        logger.info('User has activated his account!')
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'wrong code'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logger.info('User changed his password!')
        serializer = ChangePasswordSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Password changed successfully!')
    
    

class ForgotRasswordApiView(APIView):
    def post(self,request):
        logger.info('User forgot his password!')
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('We have sent you an email')
    

class ForgotPasswordFinishApiview(APIView):
    def post(self, request):
        logger.info('User reseted his password!')
        serializer = ForgotPasswordFinishSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Your password is updated successfully')