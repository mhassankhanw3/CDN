
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import ImagesCDN

def image_view(request, name):
    # Retrieve the image instance based on the name
    image_instance = get_object_or_404(ImagesCDN, name=name)

    # Return the image URL
    return HttpResponse(image_instance.image.url)
