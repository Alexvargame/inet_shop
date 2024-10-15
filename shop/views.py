from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import View

from .serializers import (CaregorySerializer,CategoryCreateSerializer,
                            ProductSerializer,ProductCreateSerializer,
                          ProductSearchSerializer,OrderUserSerializer)
from .models import Category,Product,Size
from .forms import ProductSearchForm,UserForm,ProductSearchCategoryForm
from cart.forms import CartAddProductForm
from orders.models import Order
from orders.serializers import OrderSerializer

from rest_framework.renderers import TemplateHTMLRenderer


def main_page(request):
    return render(request,'shop/main_page.html')

class CategoryListView(LoginRequiredMixin,APIView):
    def get(self,request):
        print([(c.id,c.name) for c in Category.objects.all() if c.parent is not None])
        categories=Category.objects.all()
        serializer=CaregorySerializer(categories,many=True)
        return Response(serializer.data)

class CategoryDetailView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CaregorySerializer(category)
        return Response(serializer.data)

class CategoryCreateView(LoginRequiredMixin,APIView):
    def post(self,request):
        serializer=CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            category=serializer.create(request.data)
            parent=Category.objects.get(id=request.data['parent'])
            category[0].parent=parent
            category[0].save()
            return Response(status=201)
        else:
            return Response(status=404)

class CategoryUpdateView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CaregorySerializer(category)
        return Response(serializer.data)
    def post(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CaregorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.data)
class CategoryDeleteView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CaregorySerializer(category)
        return Response(serializer.data)
    def post(self,request,pk):
        category=Category.objects.get(id=pk)
        category.delete()
        return Response(status=201)

class ProductListView(LoginRequiredMixin,APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
class ProductDetailView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

class ProductUpdateView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    def post(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.data)
class ProductDeleteView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def post(self,request,pk):
        product=Product.objects.get(id=pk)
        product.delete()
        return Response(status=201)
class ProductCreateView(LoginRequiredMixin,APIView):
    def post(self,request):
        serializer=ProductCreateSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            category=Category.objects.get(id=int(request.data['category']))
            print(category)
            product = serializer.create(request.data)
            print('p', product)
            product[0].category=category
            product[0].save()
            return Response(status=201)
        return Response(status=404)

""" Frontend"""
"""Category"""

class CategoryFrontendListView(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/categories_list.html'
    def get(self,request):
        categories=Category.objects.all()
        serializer=CaregorySerializer(categories,many=True)
        return render(request,self.template_name,{'categories':categories})

class CategoryFrontendCreateView(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/category_create.html'
    def get(self,request):
        serializer=CategoryCreateSerializer()
        print(serializer)
        return Response({'serializer':serializer})
    def post(self,request):
        serializer=CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            new_category=serializer.create(validated_data=request.data)
            new_category[0].parent=Category.objects.get(id=serializer.data['parent'])
            new_category[0].save()
            return redirect(new_category[0])
        else:
            return Response({'serializer':serializer})


class CategoryFrontendUpdateView(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/category_update.html'

    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CategoryCreateSerializer(category)
        return Response({'serializer':serializer})
    def post(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=CategoryCreateSerializer(category,data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()#create(validated_data=request.data)
            print(request.data, serializer.data)
            new_category.parent = Category.objects.get(id=serializer.data['parent'])
            new_category.save()
            return redirect(new_category)
        else:
            return Response({'serializer':serializer})

class CategoryFrontendDetailView(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/category_detail.html'
    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        serializer=ProductSerializer(category)
        return Response({'category':category})
class CategoryFrontendDeleteView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        category=Category.objects.get(id=pk)
        return render(request,'shop/category_delete.html', {'category': category})
    def post(self,request,pk):
        category=Category.objects.get(id=pk)
        category.delete()
        return redirect(reverse('categories_front_list_url'))



"""Product"""

class ProductFrontendListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/products_list.html'
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response({'products':products})


class ProductFrontendCreateView(LoginRequiredMixin,APIView):
    pass
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product_create.html'
    def get(self,request):
        initials={'length':0.0,'weight':0.0}
        serializer=ProductCreateSerializer(initial=initials)
        print(serializer)
        return Response({'serializer':serializer})
    def post(self,request):
        initials = {'length': 0.0, 'weight': 0.0}
        serializer=ProductCreateSerializer(data=request.data,initial=initials)
        if serializer.is_valid():
            print(request.data)
            new_product=serializer.create(validated_data=request.data)
            new_product.save()
            return redirect(new_product)
        else:
            return Response({'serializer':serializer})


class ProductFrontendUpdateView(LoginRequiredMixin,APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product_update.html'

    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductCreateSerializer(product)
        return Response({'serializer':serializer})
    def post(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductCreateSerializer(product,data=request.data)
        if serializer.is_valid():
            product=serializer.save()
            # new_product = serializer.save()#create(validated_data=request.data)
            # print(request.data, serializer.data)
            # new_product.parent = Product.objects.get(id=serializer.data['parent'])
            # new_product.save()
            return redirect(product)
        else:
            return Response({'serializer':serializer})

class ProductFrontendDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/product_detail.html'
    def get(self,request,slug):
        product=Product.objects.get(slug=slug)
        serializer=ProductSerializer(product)
        cart_product_form=CartAddProductForm()

        category=Category.objects.get(id=product.category.id)
        return Response({'product':product,'category':category,'cart_product_form':cart_product_form})
class ProductFrontendDeleteView(LoginRequiredMixin,APIView):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        return render(request,'shop/product_delete.html', {'product': product})
    def post(self,request,pk):
        product=Product.objects.get(id=pk)
        product.delete()
        return redirect(reverse('products_front_list_url'))

# class ProductSearchView(LoginRequiredMixin,APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'shop/product_search.html'
#     def get(self,request):
#         serializer=ProductSearchSerializer()
#         return Response({'serializer':serializer})

class ProductSearchView(LoginRequiredMixin,View):

    def get(self,request):
        initials={'price_min':0.0,'price_max':10000.0,
                  'length_min':0.0,'length_max':200.0,'weight_min':0.0,'weight_max':200.0,}
        category_list=[]
        size_list=[]
        if request.GET:
            form = ProductSearchForm(request.GET,initial=initials)
            if form['category'].value():
                category_list=form['category'].value()
            else:
                for cat in Category.objects.all():
                    category_list.append(str(cat.id))
            if form['size'].value():
                size_list=form['size'].value()
            else:
                for s in Size.objects.all():
                    size_list.append(s.size)
            serach_products=Product.objects.filter(category__in=category_list,size__in=size_list,
                                         price__range=(request.GET['price_min'],request.GET['price_max']),
                                         length__range=(request.GET['length_min'],request.GET['length_max']),
                                         weight__range=(request.GET['weight_min'],request.GET['weight_max']))
            return render(request, 'shop/products_search_list.html', {'products': serach_products})
        form = ProductSearchForm(initial=initials)
        return render(request,'shop/product_search.html',{'form':form})

def get_category_list(cat1,cat2,cat3):
    res=[]
    print('c',cat1)
    print('c', cat2)
    print('c', cat3)
    if len(cat1)>0:
        for c in cat1:
            res.extend(Category.objects.get(id=int(c)).children.all())
            for cc in Category.objects.get(id=int(c)).children.all():
                res.extend(Category.objects.get(id=cc.id).children.all())

    else:
        if len(cat2)>0:
            for c in cat2:
                res.append(Category.objects.get(id=int(c)))
                res.extend(Category.objects.get(id=int(c)).children.all())
        else:
            if len(cat3)>0:
                for c in cat3:
                    res.append(Category.objects.get(id=int(c)))
                    res.extend(Category.objects.get(id=int(c)).children.all())
    print(res)
    return res
class ProductSearchCategoryView(LoginRequiredMixin,View):

    def get(self,request):

        initials={'price_min':0.0,'price_max':10000.0,
                  'length_min':0.0,'length_max':200.0,'weight_min':0.0,'weight_max':200.0,}
        category_list=[]
        size_list=[]
        if request.GET:
            print(request.GET)
            form = ProductSearchCategoryForm(request.GET,initial=initials)
            category_list=get_category_list(form['category_1'].value(),form['category_2'].value(),form['category_3'].value())
            # if form['category'].value():
            #     category_list=form['category'].value()
            # else:
            #     for cat in Category.objects.all():
            #         category_list.append(str(cat.id))
            if form['size'].value():
                size_list=form['size'].value()
            else:
                for s in Size.objects.all():
                    size_list.append(s.size)
            serach_products=Product.objects.filter(category__in=category_list,size__in=size_list,
                                         price__range=(request.GET['price_min'],request.GET['price_max']),
                                         length__range=(request.GET['length_min'],request.GET['length_max']),
                                         weight__range=(request.GET['weight_min'],request.GET['weight_max']))
            return render(request, 'shop/products_search_list.html', {'products': serach_products})

        form = ProductSearchCategoryForm(initial=initials)
        return render(request,'shop/product_category_search.html',{'form':form})


class OrdersUserList(LoginRequiredMixin,View):
    def get(self,request):
        if request.GET:
            form=UserForm(request.GET)
            orders=Order.objects.filter(username=request.GET['search_user'])
            #back_str='?'+'csrfmiddlewaretoken'+'='+request.GET['csrfmiddlewaretoken']+'&'+'search_user'+'='+request.GET['search_user']
            return render(request,'shop/user_orders_list.html',{'orders':orders,'form':form})
        else:
            form=UserForm()
            return render(request,'shop/user_orders_list.html',{'form':form})

class OrdersUserListForName(LoginRequiredMixin,View):
    def get(self,request,name):
        print('N',name)
        orders=Order.objects.filter(username=name)
        print(orders)
        form = UserForm()
        return render(request, 'shop/user_orders_list.html', {'orders':orders,'form':form})
