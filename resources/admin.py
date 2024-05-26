from django.contrib import admin
from .models import Tip

# Register your models here.
class TipAdmin(admin.ModelAdmin):
    list_filter = ("author", "date",)
    list_display = ("id", "title", "available", "feature", "date", "author",)
    list_editable = ('available', 'feature')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tip, TipAdmin)

