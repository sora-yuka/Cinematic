from rest_framework import serializers
from django.db.models import Avg
from applications.films.models import Films, Genre
from applications.feedback.models import Like, Rating


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'
        
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = Like.objects.filter(films=instance, is_like=True).count()
        rating = Rating.objects.filter(films=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            representation['rating'] = rating
        representation['rating'] = 0
        return representation
        

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'