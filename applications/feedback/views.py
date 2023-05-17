import logging
from django.shortcuts import get_object_or_404
from applications.feedback.models import Favorite, Like, Rating, Comment
from applications.feedback.serializers import FavoriteSerializer
from applications.feedback.permissions import IsFeedBackOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

logger = logging.getLogger('main')


class SavedAPIView(APIView):
    permission_classes = [IsFeedBackOwner]
    
    def get(self, request):
        films = Favorite.objects.filter(owner=request.user)
        serializer = FavoriteSerializer(films, many=True)
        return Response(serializer.data)
    
class SavedDetailAPIView(APIView):
    permission_classes = [IsFeedBackOwner]
    
    def get(self, request, pk):
        try:
            films = Favorite.objects.get(pk=pk)
            serializer = FavoriteSerializer(films)
            return Response(serializer.data)
        except Favorite.DoesNotExist:
            return Response("Not found!", status=status.HTTP_404_NOT_FOUND)