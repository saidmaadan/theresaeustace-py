from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from accounts.models import Account



class Tip(models.Model):
    title        = models.CharField(max_length=150)
    date         = models.DateField(auto_now=True)
    slug         = models.SlugField(unique=True, db_index=True)
    source_url   = models.CharField(max_length=500)
    content      = models.TextField(validators=[MinLengthValidator(10)])
    available    = models.BooleanField(default=True)
    feature      = models.BooleanField(default=False)
    image        = models.ImageField(upload_to="posts", null=True)
    author       = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, related_name="listings")
    

    def __str__(self):
        return self.title

