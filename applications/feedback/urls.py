from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import LikeModelViewSet, CommentModelViewSet, RatingModelViewSet, FavoriteModelViewSet

router = DefaultRouter()
router.register('like', LikeModelViewSet, basename='like')
router.register('comment', CommentModelViewSet, basename='comment')
router.register('rating', RatingModelViewSet, basename='rating')
router.register('favorite', FavoriteModelViewSet, basename='favorite')

urlpatterns = [
    # path('rating/', include(router.urls)),
    # path('like/', include(router.urls)),
    # path('comment/', include(router.urls)),
    path('', include(router.urls))
]
# urlpatterns += router.urls
