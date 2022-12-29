
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('store/', views.ItemList.as_view(), name='store'),
    path('store/<int:pk>/', views.ItemDetail.as_view(), name='item'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),  
]
