import logging
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from applications.films.models import Films, Genre
from applications.films.serializers import FilmsSerializer, GenreSerializers
from applications.films.permissions import IsAdmin, FeedBack
from applications.feedback.models import Like, Rating, Favorite
from applications.feedback.serializers import RatingSerializer

logger = logging.getLogger('main')

class PaginationApiView(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'films'


class FilmsViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer
    
    def list(self, request, *args, **kwargs):
        logger.info('Listing films...')
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        logger.info('Posting a film...')
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        logger.info('Updating a film...')
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        logger.info('Deleting a film...')
        return super().destroy(request, *args, **kwargs)
    
    pagination_class = PaginationApiView
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'director', 'genres']
    search_fields = ['title', 'director']
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_permissions(self):
        action = ['like', 'rating', 'save']
        if self.action in action:
            return [FeedBack()]
        return super().get_permissions()
    
    @action(detail=True, methods=["POST"])
    def like(self, request, pk, *args, **kwargs):
        like_obj, created = Like.objects.get_or_create(
            owner = request.user,
            films_id = pk,
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
            films_id = pk,
        )
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=["POST"])
    def save(self, request, pk, *args, **kwargs):
        saved_obj, created = Favorite.objects.get_or_create(
            owner = request.user,
            films_id = pk,
        )
        message = 'Added to favorite'
        saved_obj.save()
        if not created:
            saved_obj.delete()
            message = 'Deleted from favorite'
        return Response({"message": message})
    

class GenreViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers