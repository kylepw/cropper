from django.db import models
from django.utils import timezone

from .utils import generate_hash


class URL(models.Model):
    url = models.URLField(unique=True)
    url_hash = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def mins_since_created(self):
        return ((timezone.now() - self.created).seconds//60) % 60
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.url} ({self.url_hash})'

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = generate_hash(URL)
        return super().save(*args, **kwargs)