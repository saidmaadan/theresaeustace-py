from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.book, name='book'),
    path('books/<slug:collection_slug>/', views.book, name='books_by_collection'),
    path('book/<slug:collection_slug>/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:book_id>/', views.submit_review, name='submit_review'),
    # path("upload/", custom_upload_function, name="custom_upload_file"),
]