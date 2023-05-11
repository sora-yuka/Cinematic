from rest_framework import serializers

from applications.films.models import Films


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        