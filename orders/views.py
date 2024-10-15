from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User


from .models import OrderItem,Order
from .forms import OrderCreateForm
from .serializers import OrderSerializer,OrderItemSerializer
from cart.cart import Cart
from django.contrib.auth.mixins import LoginRequiredMixin

from discont.models import DiscontCard

class OrderCreateView(View):

    def get(self,request):
        cart=Cart(request)
        if request.user.is_authenticated:
            initials = {'username': request.user.username,'phone_number':request.user.profile.get_phone_number()[0]}
            form=OrderCreateForm(initial=initials)
        else:
            form=OrderCreateForm()
        return render(request,'orders/create.html', {'cart': cart, 'form': form})
    def post(self,request):
        cart = Cart(request)
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            if request.user.is_authenticated:
                discont=DiscontCard.objects.get(user=request.user)
                discont.active=True
                discont.save()
            return render(request, 'orders/created.html', {'order': order})
        else:
            form = OrderCreateForm()
            return render(request, 'orders/create.html', {'cart': cart, 'form': form})


class OrderDetail(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders/order_detail.html'
    def get(self,request,pk):
        order=Order.objects.get(id=pk)
        serializer=OrderSerializer(order)
        return Response({'order':order})

class OrderItemDetail(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders/order_item_detail.html'
    def get(self,request,pk):
        orderitem=OrderItem.objects.get(id=pk)
        serializer=OrderItemSerializer(orderitem)
        return Response({'orderitem':orderitem})
