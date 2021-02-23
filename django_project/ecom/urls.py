from django.urls import path
#from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Product/', views.Product, name='Product'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    path('Post/<int:id>/', views.Post, name='Post'),
    path('addproducts/', views.addproducts, name='addproducts'),
    
]