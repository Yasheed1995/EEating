from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid 

# Create your models here.
class Genre(models.Model):
    '''
    Model representing a product genre (e.g. Seafood, Pork)
    '''
    name = models.CharField(max_length=200, help_text='Enter a product genre (e.g. Seafood, Beef etc.)')

    def __str__(self):
        '''
        str
        '''
        return self.name

class Product(models.Model):
    '''
    Model representing a product (but not a specific copy of a product)
    '''
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    seller = models.ForeignKey('Seller', on_delete=models.SET_NULL, null=True)
    note = models.TextField(max_length=1000, help_text = 'Enter a brief description of the product')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this product')

    def __str__(self):
        '''
        String for represent the Model object.
        '''
        return self.name

    def get_absolute_url(self):
        '''
        returs the url to access a detail record for this product
        '''
        return reverse('product-detail', args=[str(self.id)])
    
class ProductInstance(models.Model):
    '''
    Model representing a specific copy of a product
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this product')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    due = models.DateField(null=True, blank=True)
    
    SELL_STATUS = (
        ('o', 'Sold out'),
        ('m', 'On sale'),
        ('r', 'reserved'),
        ('n', 'normal'),
        ('l', 'Low quantity')
    )
    
    status = models.CharField(max_length=1, choices=SELL_STATUS, blank=True, default='n', help_text='Product Information')

    class Meta:
        ordering = ['due']

    def __str__(self):
        '''
        Strig for 
        '''
        return '{0}, ({1})'.format(self.id, self.product.name)
         
class Seller(models.Model):
    '''
    Model representing a seller.
    '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        '''
        Returns the url to access
        '''
        return reverse('seller-detail', args=[str(self.id)])

    def __str__(self):
        '''
        String for
        '''
        return '{0}, {1}'.format(self.last_name, self.first_name)
