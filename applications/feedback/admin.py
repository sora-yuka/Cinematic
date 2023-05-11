from django.contrib import admin
from applications.feedback.models import Like, Rating, Favorite, Comment

admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Comment)