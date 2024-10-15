from django.urls import path
from . import views

app_name='orders'
urlpatterns=[
   # path('create/',views.order_create,name='order_create'),
    path('create/',views.OrderCreateView.as_view(),name='order_create'),
    path('<int:pk>/',views.OrderDetail.as_view(),name='order_detail_url'),
    path('orderitem/<int:pk>/',views.OrderItemDetail.as_view(),name='orderitem_detail_url'),

]