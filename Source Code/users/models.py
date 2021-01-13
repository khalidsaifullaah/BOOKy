from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(default="", max_length=80)
    contact_no  = models.CharField(max_length=11, null=True, blank=True)
    buyer_rating = models.IntegerField(default=0, null=True, blank=True)
    seller_rating = models.IntegerField(default=0, null=True, blank=True)
    total_seller_ratings = models.IntegerField(default=0, null=True, blank=True)
    total_buyer_ratings = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)

        # ImageOps compatible mode
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        imagefit = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
        imagefit.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'
