from django.contrib import admin
from .models import Book, Tag, BookGallery, ReviewRating
import admin_thumbnails
from django.utils.html import format_html
# Register your models here.

@admin_thumbnails.thumbnail('image')
class BookGalleryInline(admin.TabularInline):
    model = BookGallery
    extra = 1

class BookAdmin(admin.ModelAdmin):
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.images.url))

    # thumbnail.short_description = 'Image'

    list_filter = ( 'collection', 'tags', 'created_date',)
    list_display = ('id', 'title', 'price', 'pre_order', 'is_feature', 'stock', 'is_new_released', 'collection', 'modified_date', 'is_available', 'is_home_scroll')
    list_editable = ('is_available', 'pre_order', 'is_feature', 'is_home_scroll', 'is_new_released')
    list_display_links = ('id',  'title')
    search_fields = ('id', 'title', 'price', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BookGalleryInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Tag)
admin.site.register(BookGallery)
admin.site.register(ReviewRating)


