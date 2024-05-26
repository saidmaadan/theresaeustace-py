from django.db import models
from django.urls import reverse

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    

    class Meta:
        verbose_name = 'collection'
        verbose_name_plural = 'collections'

    def get_url(self):
        return reverse('books_by_collection', args=[self.slug])

    def __str__(self):
        return self.collection_name
