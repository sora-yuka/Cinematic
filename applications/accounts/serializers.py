from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.accounts.tasks import send_act_code

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length = 6, required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name']
        
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Passwords are not similar')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        code = user.activation_code
        send_act_code(user.email, code)
        user.save()
        return user
    
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password2 = serializers.CharField(required=True, min_length=6)
    
    def validate(self, attrs):
        p = attrs.get('new_password')
        p2 = attrs.get('new_password2')
        if p != p2:
            raise serializers.ValidationError('Passwords are not similar!')
        return attrs
    
    def validate_old_password(self, password):
        user = self.context.get('request').user
        if not user.check_password(password):
            raise serializers.ValidationError('Current password is wrong')
        return password
    
    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()
    