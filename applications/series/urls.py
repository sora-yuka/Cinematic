from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.series.views import (
    SeriesModelViewSet, SeasonModelViewSet, TrailerModelViewSet, GenreModelViewSet
)

router = DefaultRouter()
router.register("genre", GenreModelViewSet)
router.register("trailer", TrailerModelViewSet)
router.register("season", SeasonModelViewSet)
router.register("", SeriesModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]