from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from applications.feedback.models import Like, Rating, Favorite
from applications.feedback.serializers import RatingSerializer
from applications.series.models import Series, Season, Episodes, Genre, Trailer
from applications.series.permissions import IsAdmin, FeedBack
from applications.series.serializers import (
    SeriesSerializer, SeasonSerializer, EpisodeSerializer, GenreSerializer, TrailerSerializer
)


class SeriesModelViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdmin]
    
    def get_permissions(self):
        action = ['like', 'rating', 'save']
        if self.action in action:
            return [FeedBack()]
        return super().get_permissions()
    
    @action(detail=True, methods=["POST"])
    def like(self, request, pk, *args, **kwargs):
        like_obj, created = Like.objects.get_or_create(
            owner = request.user,
            series_id = pk,
        )
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked' if like_obj.is_like else 'unliked'
        return Response({'status': status})
    
    @action(detail=True, methods=["POST"])
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, created = Rating.objects.get_or_create(
            owner = request.user,
            series_id = pk,
        )
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=["POST"])
    def save(self, request, pk, *args, **kwargs):
        saved_obj, created = Favorite.objects.get_or_create(
            owner = request.user,
            series_id = pk,
        )
        message = 'Added to favorite'
        saved_obj.save()
        if not created:
            saved_obj.delete()
            message = 'Deleted from favorite'
        return Response({"message": message})
    

class SeasonModelViewSet(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsAdmin]
    

class TrailerModelViewSet(ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
    permission_classes = [IsAdmin]
    

class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdmin]