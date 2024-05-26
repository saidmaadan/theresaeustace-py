from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('terms_and_conditions', views.terms, name='terms'),   
    path('privacy_policy', views.privacy, name='privacy'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('contact', views.contact, name='contact'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('already-subscribed', views.already_subscribed, name='already-subscribed'),

    

]
