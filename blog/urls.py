from django.urls import path

from . import views

urlpatterns = [
    path('post/<slug:category_slug>/', views.AllPostsView.as_view(), name='posts_by_category'),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    path("post/<slug:category_slug>/<slug:post_slug>/", views.SinglePostView.as_view(),
         name="post-detail"),  # /posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    # path('search/', views.SearchView.as_view(), name='search')
    path('search/', views.search, name='search'),
]