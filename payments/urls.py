from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Payments/<int:product_id>', views.payments, name='payments'),
    path('Wishlist/<int:product_id>', views.wishlist, name='wishlist'),
    path('Cart/', views.cart, name='View Cart'),
    path('wishlistView/', views.wishlistView, name='wishlist View'),
    path('deleteitem/<int:id>', views.deleteitem, name='Cart Item Delete'),
    path('wishlistdeleteitem/<int:id>', views.wishlistdeleteitem, name='Wishlist Item Delete'),
    path('paymentpage', views.paymentpage, name='paymentpage'),
    path('ordercomplete', views.ordercomplete, name='ordercomplete'),
    path('myorders', views.myorders, name='myorders'),

]
