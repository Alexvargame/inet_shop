from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order,OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=('username','name','email','phone_number')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=('order','product','price','quantity')
