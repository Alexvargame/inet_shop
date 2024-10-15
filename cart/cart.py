from django.conf import settings
from decimal import Decimal
from shop.models import Product
from django.contrib.auth.models import User
from discont.models import DiscontCard
from .forms import CartAddProductForm
class Cart(object):
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
        if request.user.is_authenticated:
            self.discont=DiscontCard.objects.get(user=request.user)
        else:
            self.discont=None
    def add(self,product,quantity=1,update_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()
        print('CCAR',self.cart,self.discont.pension+self.discont.accumulative)
    def save(self):
        self.session.modified=True
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    def __iter__(self):
        if self.discont:
            if self.discont.pension:
                discont=(settings.DISCONT_PENSION+self.discont.accumulative/100)
            else:
                discont = self.discont.accumulative/100
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():
            item['discont']=Decimal(float(item['price'])*discont).quantize(Decimal("1.00"))
            item['price']=item['price']
            item['total_price']=(Decimal(item['price'])-Decimal(item['discont']))*item['quantity']
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
            yield item
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def get_total_price(self):
        if self.discont.active is True:
            return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())-settings.FIRST_DISCOUNT

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
