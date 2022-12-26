from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('store/', views.store, name='store'),
    path('cart/', views.store, name='cart'),
    path('checkout/', views.store, name='checkout'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),
    
]
