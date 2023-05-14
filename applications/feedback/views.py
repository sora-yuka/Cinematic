import logging
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import generics
from rest_framework import mixins, viewsets
from applications.feedback.models import Favorite, Like, Rating, Comment
from applications.feedback.serializers import FavoriteSerializer, LikeSerializer, RatingSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

logger = logging.getLogger('main')

class LikeViewSet(viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        try:
            like_obj = Like.objects.get(owner=user, post_id=pk)
            status = 'unliked'
            like_obj.delete()
        except Like.DoesNotExist:
            like_obj = Like(owner=user, post_id=pk, is_like=True)
            like_obj.save()
            status = 'liked'
        
        return Response({'status': status})
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingViewSet(viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class CommentModelMixin(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                #    mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class FavoriteViewSet(viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
