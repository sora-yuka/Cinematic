
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(
    title = 'Cinematic',
    default_version = '1.0',
    description = 'This is cinematic swagger'
),  public = True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.accounts.urls')),
    path('api/v1/profile/', include('applications.profiles.urls')),
    path('api/v1/films/', include('applications.films.urls')),
    path('api/v1/feedback/', include('applications.feedback.urls')),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)