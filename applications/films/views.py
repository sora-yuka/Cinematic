from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from applications.films.models import Films
from applications.films.serializers import FilmsSerializer
from applications.films.permissions import IsAdmin

class PaginationApiView(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'films'


class FilmsViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer
    
    pagination_class = PaginationApiView
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'director', ]
    search_fields = ['title', 'director']
    