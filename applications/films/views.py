import logging
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from applications.films.models import Films, Genre
from applications.films.serializers import FilmsSerializer, GenreSerializers
from applications.films.permissions import IsAdmin

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
    

class GenreViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers