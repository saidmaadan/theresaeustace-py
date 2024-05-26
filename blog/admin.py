from django.contrib import admin
from .models import Post, Tag, PostGallery, Comment
import admin_thumbnails
from django.utils.html import format_html

# Register your models here.
@admin_thumbnails.thumbnail('image')
class PostGalleryInline(admin.TabularInline):
    model = PostGallery
    extra = 1

class PostAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Image'

    list_filter = ("author", "category", "tags", "date",)
    list_display = ("id", "thumbnail", "title", "time_to_read", "is_popular", "is_available", "is_feature", "is_home_feature", "category", "date", "author",)
    list_editable = ('time_to_read', 'is_available', 'is_feature', 'is_home_feature', 'is_popular',)
    list_display_links = ('id', 'thumbnail', 'title',)
    search_fields = ('id', 'title', )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostGalleryInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(PostGallery)
admin.site.register(Comment, CommentAdmin)