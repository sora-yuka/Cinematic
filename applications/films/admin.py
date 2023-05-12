from django.contrib import admin

from applications.films.models import Films, Genre

admin.site.register(Films)
admin.site.register(Genre)