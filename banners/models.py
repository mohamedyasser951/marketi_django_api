from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title or "Banner"
