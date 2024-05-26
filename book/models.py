from django.db import models
from collection.models import Collection
from django.urls import reverse
from accounts.models import Account

# from django_ckeditor_5.fields import CKEditor5Field

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
      return self.caption

class Book(models.Model):
    title           = models.CharField(max_length=300, unique=True)
    sub_title       = models.CharField(max_length=400, blank=True, null=True)
    slug            = models.SlugField(max_length=300, unique=True)
  # description     = CKEditor5Field('Text', config_name='extends')
    description     = models.TextField(max_length=1000, blank=True, null=True)
    price           = models.CharField(blank=True, null=True)
    
    discount        = models.IntegerField(blank=True, null=True)
    images          = models.ImageField(upload_to='photos/book', blank=True, null=True)
    stock           = models.IntegerField(blank=True, null=True)
    is_available    = models.BooleanField(default=True)
    is_feature      = models.BooleanField(default=False)
    pre_order       = models.BooleanField(default=False)
    is_home_scroll  = models.BooleanField(default=False)
    is_new_released = models.BooleanField(default=False)
    amazon_url      = models.CharField(max_length=400, blank=True, null=True)
    apple_url       = models.CharField(max_length=400, blank=True, null=True)
    barnes_url      = models.CharField(max_length=400, blank=True, null=True)
    kobo_url        = models.CharField(max_length=400, blank=True, null=True)
    buy_now_url     = models.CharField(max_length=400, blank=True, null=True)
    free_download_url   = models.CharField(max_length=1000, blank=True, null=True)
    author          = models.CharField(max_length=400, blank=True, null=True)
    published_date  = models.DateTimeField(blank=True, null=True)
    available_in    = models.CharField(max_length=200, blank=True, null=True)
    collection      = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    tags            = models.ManyToManyField(Tag, blank=True, null=True)

    def get_url(self):
        return reverse('book_detail', args=[self.collection.slug, self.slug])

    def __str__(self):
        return self.title

class BookGallery(models.Model):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/books', blank=True, null=True)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'bookgallery'
        verbose_name_plural = 'book gallery'

class ReviewRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_email

