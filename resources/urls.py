from django.urls import path
from . import views

urlpatterns = [
    path("tip", views.StartingPageView.as_view(), name="starting-page"),
    path("", views.AllTipsView.as_view(), name="tips-page"),
    path("<slug:slug>", views.SingleTipView.as_view(),
         name="tip-detail"),
    path('search_/', views.search_resources, name='search_'),
]
