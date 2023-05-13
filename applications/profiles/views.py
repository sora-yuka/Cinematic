import logging
from rest_framework.viewsets import mixins, GenericViewSet

from applications.profiles.models import Profile
from applications.profiles.permissions import IsProfileOwner
from applications.profiles.serializers import ProfileSerializer

logger = logging.getLogger('main')

class ProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner]
    queryset = Profile.objects.filter()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def list(self, request, *args, **kwargs):
        logger.info('User looking his profile!')
        return super().list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        logger.info('User updating profile!')
        return super().update(request, *args, **kwargs)