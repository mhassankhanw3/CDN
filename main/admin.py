from django.contrib import admin
from .models import ImagesCDN


@admin.register(ImagesCDN)
class ImagesCDNAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
