from rest_framework import serializers
from applications.feedback.models import Like, Rating, Favorite, Comment

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email', required=False)

    class Meta:
        model = Like
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=10)
    owner = serializers.ReadOnlyField(source='owner.email', required=False)

    class Meta:
        model = Rating
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Favorite
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {key: value for key, value in representation.items() if value is not None}


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"