from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('room-details/', views.room_details, name='room_details'),
    path('amenities/', views.amenities, name='amenities'),
    path('location/', views.location, name='location'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('offers/', views.offers, name='offers'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]