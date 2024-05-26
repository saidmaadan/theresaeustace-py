from django.contrib import admin
from .models import Collection

# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('collection_name',)}
    list_display = ('collection_name', 'slug')

admin.site.register(Collection, CollectionAdmin)
