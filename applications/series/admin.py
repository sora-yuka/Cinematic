from django.contrib import admin
from applications.series import models

# Register your models here.
admin.site.register(models.Series)
admin.site.register(models.Season)
admin.site.register(models.Episodes)
admin.site.register(models.Trailer)
admin.site.register(models.Genre)