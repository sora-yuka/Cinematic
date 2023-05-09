from rest_framework import serializers

from applications.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = '__all__'