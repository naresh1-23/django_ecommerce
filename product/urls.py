from django.urls import path
from . import views
from user.views import search
urlpatterns = [
    path("", views.home, name = 'home' ),
    path("addproduct/", views.add_product, name = 'add-product'),
    path("search/", search , name = 'search'),
    path('product/<int:pk>', views.SingleProduct, name = 'product'),
    path("cart/", views.cart, name = 'cart'),
    path("deletecart/<int:pk>/", views.delete_cart, name = 'delete-cart'),
    path('order/<int:pk>/',views.order_cart, name = 'order-cart'),
    path('order/', views.ordersUser, name = 'order'),
    path('ordersAdmin/', views.admin_order, name = 'admin-order')
]