from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import LikeModelViewSet, CommentModelViewSet, RatingModelViewSet, FavoriteModelViewSet

router = DefaultRouter()
router.register('like', LikeModelViewSet, basename='like')
router.register('comment', CommentModelViewSet, basename='comment')
router.register('rating', RatingModelViewSet, basename='rating')
router.register('favorite', FavoriteModelViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls))
]