from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.series.permissions import IsAdmin
from applications.series.models import Series, Season, Episodes, Genre, Trailer
from applications.series.serializers import (
    SeriesSerializer, SeasonSerializer, EpisodeSerializer, GenreSerializer, TrailerSerializer
)


class SeriesModelViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdmin]
    

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