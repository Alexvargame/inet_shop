from django.db import models
from shop.models import Product
from django.shortcuts import reverse

class Order(models.Model):
    username=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phone_number=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    def get_absolute_url(self):
        return reverse('orders:order_detail_url',kwargs={'pk':self.id})

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price*self.quantity
    def get_absolute_url(self):
        return reverse('orders:orderitem_detail_url',kwargs={'pk':self.id})

