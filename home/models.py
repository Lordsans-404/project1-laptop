from django.db import models
from django.utils.text import slugify
from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField
import random
from django.http import JsonResponse, HttpResponseRedirect



class Category(models.Model):
    name            = models.CharField(max_length=255)
    logo_category   = models.ImageField(null=True,blank=True,upload_to='logo/')
    slug            = models.SlugField(null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.logo_category.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category        = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255,unique=True)
    img_product1    = models.ImageField(null=True,blank=True,upload_to='image/')
    img_product2    = models.ImageField(null=True,blank=True,upload_to='image/')
    old_price       = models.DecimalField(blank=True,null=True,max_digits=8,decimal_places=3)
    price           = models.DecimalField(max_digits=8,decimal_places=3)
    description     = models.TextField()
    upload_time     = models.DateField(auto_now_add=True)
    stock           = models.IntegerField(default=1)
    slug            = models.SlugField(blank=True)

    @property
    def imageURL1(self):
        try:
            url_1 = self.img_product1.url
        except:
            url_1 = '/static/empty.png'
        return url_1

    @property
    def imageURL2(self):
        try:
            url_2 = self.img_product2.url
        except:
            url_2 = '/static/empty.png'
        return url_2

    def save(self):
        self.slug = slugify(self.name)
        super(Product,self).save()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return str(self.id)

    def save(self,*args,**kwargs):
        anjay = random.randrange(100,99999999)
        self.transaction_id = anjay
        super(Order,self).save()

    @property
    def get_cart_totals(self):
        orderitem = self.orderitem_set.all()
        return sum([item.get_total for item in orderitem])
   
    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        return sum([item.quantity for item in orderitem])
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, blank=True)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, blank=True)
    quantity = models.IntegerField(default=0, null=True,blank=True) 
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        print(self.quantity)
        return self.product.price * self.quantity

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, blank=True)
    email = models.EmailField(max_length=200,null=True)
    kota = models.CharField(max_length=255,default='bogor')
    address = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('homey:index')