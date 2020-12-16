from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image, ImageOps


class Book(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.TextField(default="", max_length=50)
    cover = models.ImageField(default='default.jpg', upload_to='book_covers')
    no_of_pages = models.IntegerField()
    price = models.IntegerField()
    authors = models.TextField(default="", max_length=30)
    publications = models.TextField(default="", max_length=20)
    synopsis = models.TextField(default="", max_length=200)
    upload_date = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.cover.path)

        # ImageOps compatible mode
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        imagefit = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
        imagefit.save(self.cover.path)


    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title
    
