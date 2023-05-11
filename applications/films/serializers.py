from rest_framework import serializers

from applications.films.models import Films, Genre


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
