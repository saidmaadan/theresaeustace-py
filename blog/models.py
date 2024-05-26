from django.db import models
from category.models import Category
from django.core.validators import MinLengthValidator
from django.urls import reverse
from accounts.models import Account


class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self):
      return self.caption


class Post(models.Model):
    title           = models.CharField(max_length=300)
    slug            = models.SlugField(unique=True, db_index=True)
    content         = models.TextField(validators=[MinLengthValidator(20)])    
    # headline        = models.TextField(validators=[MinLengthValidator(10)])
    image           = models.ImageField(upload_to="posts", null=True)
    time_to_read    = models.CharField(max_length=200, blank=True, null=True)
    is_available    = models.BooleanField(default=True)
    is_feature      = models.BooleanField(default=False)
    is_popular      = models.BooleanField(default=False)
    is_home_feature = models.BooleanField(default=False)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    author          = models.ForeignKey(
                        Account, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags            = models.ManyToManyField(Tag, blank=True, null=True)

    date            = models.DateField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now_add=True)       

    def get_url(self):
        return reverse('post-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title

class PostGallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/images', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'postgallery'
        verbose_name_plural = 'Post Galleries'


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_email
