from .models import Collection

def collection_menu_links(request):
    links = Collection.objects.all()
    return dict(collection_links=links)
