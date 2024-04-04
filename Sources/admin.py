from django.contrib import admin
from .models import ExternalReview, ExternalUser, ExternalAnimeTitle, ExternalSource
# Register your models here.

admin.site.register(ExternalUser)
admin.site.register(ExternalAnimeTitle)
admin.site.register(ExternalSource)
admin.site.register(ExternalReview)