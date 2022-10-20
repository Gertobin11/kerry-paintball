from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField(default=39)
    synopsis = models.TextField()
    content = models.TextField()
    img = models.ImageField(upload_to="package_images")

    def __str__(self):
        return self.title
