
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('store/', views.itemList, name='store'),
    path('store/<int:id>/', views.itemDetail, name='item'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'), 

    path('update_item/', views.updateItem, name='update_item'),
    path('create_order/', views.creatingOrder, name = 'create_order') 
]
