
from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page,name='main_page_url'),
    path('shop/categories/',CategoryListView.as_view(),name='categories_list_url'),
    path('shop/categories/<int:pk>/',CategoryDetailView.as_view(),name='category_detail_url'),
    path('shop/categories/create/',CategoryCreateView.as_view(),name='category_create_url'),
    path('shop/categories/<int:pk>/update/',CategoryUpdateView.as_view(),name='category_update_url'),
    path('shop/categories/<int:pk>/delete/',CategoryDeleteView.as_view(),name='category_delete_url'),
    path('shop/categories/front/',CategoryFrontendListView.as_view(),name='categories_front_list_url'),
    path('shop/categories/front/<int:pk>/',CategoryFrontendDetailView.as_view(),name='category_front_detail_url'),
    path('shop/categories/front/create/',CategoryFrontendCreateView.as_view(),name='category_front_create_url'),
    path('shop/categories/front/<int:pk>/update/',CategoryFrontendUpdateView.as_view(),name='category_front_update_url'),
    path('shop/categories/front/<int:pk>/delete/',CategoryFrontendDeleteView.as_view(),name='category_front_delete_url'),
    path('shop/products/',ProductListView.as_view(),name='products_list_url'),
    path('shop/products/create/',ProductCreateView.as_view(),name='product_create_url'),
    path('shop/products/<int:pk>/',ProductDetailView.as_view(),name='product_detail_url'),
    path('shop/products/<int:pk>/update/',ProductUpdateView.as_view(),name='product_update_url'),
    path('shop/products/<int:pk>/delete/',ProductDeleteView.as_view(),name='product_delete_url'),
    path('shop/products/front/',ProductFrontendListView.as_view(),name='products_front_list_url'),
    path('shop/products/front/create/',ProductFrontendCreateView.as_view(),name='product_front_create_url'),

    path('shop/products/front/<int:pk>/update/',ProductFrontendUpdateView.as_view(),name='product_front_update_url'),
    path('shop/products/front/<int:pk>/delete/',ProductFrontendDeleteView.as_view(),name='product_front_delete_url'),
    path('shop/products/front/search/',ProductSearchView.as_view(),name='product_front_search_url'),
    path('shop/products/front/search/category/',ProductSearchCategoryView.as_view(),name='product_front_category_search_url'),
    path('shop/products/front/user_orders/',OrdersUserList.as_view(),name='orders_front_user_list_url'),
    path('shop/products/front/<str:slug>/',ProductFrontendDetailView.as_view(),name='product_front_detail_url'),
    path('shop/products/front/user_orders/<str:name>/',OrdersUserListForName.as_view(),name='orders_front_user_for_name_list_url'),
]
