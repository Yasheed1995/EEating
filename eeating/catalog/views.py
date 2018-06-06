from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
def index(request):
     '''
     View function for home page of site.
     '''
     num_products = Product.objects.all().count()
     num_instances = ProductInstance.objects.all().count()
     num_instances_onSale = ProductInstance.objects.filter(status__exact='m').count()
     num_sellers = Seller.objects.count()
 
     return render(
         request,
         'index.html',
         context={
            'num_products': num_products,
            'num_instances': num_instances,
            'num_instances_onSale': num_instances_onSale,
            'num_sellers': num_sellers
         },
     )

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product
