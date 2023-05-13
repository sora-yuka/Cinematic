from rest_framework import serializers
from django.db.models import Avg
from applications.series.models import Series, Season, Episodes, Genre, Trailer
from applications.feedback.models import Like, Rating


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = "__all__"


class SeriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Series
        fields = "__all__"
        
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["like"] = Like.objects.filter(films=instance, is_like=True).count()
    #     representation["ratings"] = Rating.objects.filter(films=insstance).aggregate(Avg("rating"))["rating__avg"]
    #     return representation
        

class SeasonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Season
        fields = "__all__"
        

class EpisodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Episodes
        fields = "__all__"
        

class TrailerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trailer
        fields = "__all__"