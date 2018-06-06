#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('products/', views.ProductListView.as_view(), name='products'),
    url('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]

