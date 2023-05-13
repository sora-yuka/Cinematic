from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import CommentModelMixin, RatingViewSet, FavoriteViewSet, LikeViewSet

router = DefaultRouter()
router.register('like', LikeViewSet, basename='like')
router.register('comment', CommentModelMixin, basename='comment')
router.register('rating', RatingViewSet, basename='rating')
router.register('favorite', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]