from django.views.generic import ListView
from .models import GalleryImage


class GalleryView(ListView):
    model = GalleryImage
    template_name = 'gallery.html'
