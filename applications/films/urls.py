from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.films.views import FilmsViewSet


router = DefaultRouter()
router.register('', FilmsViewSet)


urlpatterns = [
    path('', include(router.urls))
]
