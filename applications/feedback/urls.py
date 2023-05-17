from django.urls import path
from applications.feedback.views import SavedAPIView, SavedDetailAPIView

urlpatterns = [
    path('saved/', SavedAPIView.as_view()),
    path('saved/<int:pk>/', SavedDetailAPIView.as_view()),
]