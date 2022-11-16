from django.db import models
from django.urls import reverse


class Package(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField(default=39)
    synopsis = models.TextField()
    content = models.TextField()
    img = models.ImageField(upload_to="package_images")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('package_detail', args=[(self.pk)])
