from django.db import models


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
