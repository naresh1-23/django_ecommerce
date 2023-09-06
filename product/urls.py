from django.urls import path
from . import views
from user.views import search
urlpatterns = [
    path("", views.home, name = 'home' ),
    path("addproduct/", views.add_product, name = 'add-product'),
    path("search/", search , name = 'search')
]