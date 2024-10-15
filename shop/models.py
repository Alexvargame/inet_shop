from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import reverse
class Category(MPTTModel):
    name=models.CharField(max_length=100)
    parent=TreeForeignKey('self',related_name='children',on_delete=models.SET_NULL,null=True,blank=True)

    class MPTTMEta:
        order_insertion_by=['name']
        verbose_name='Категория'
        verbose_name_plural='Категории'
    def __str__(self):
        if self.parent is None:
            return self.name
        return f'{self.parent}: {self.name}'

    def get_children(self):
        return [cat for cat in self.children.all()]
    def get_products(self):
        return self.product_category.all()
    def get_absolute_url(self):
        return reverse('category_front_detail_url',kwargs={'pk':self.id})
    def get_update_url(self):
        return reverse('category_front_update_url',kwargs={'pk':self.id})
    def get_delete_url(self):
        return reverse('category_front_delete_url',kwargs={'pk':self.id})

class Size(models.Model):
    size=models.CharField(max_length=10)
    class Meta:
        verbose_name='Размер'
        verbose_name_plural='Размеры'
    def __str__(self):
        return self.size


def limit_category():
    print([c for c in Category.objects.all() if c.parent is True])
    return {'parent': True,}
class Product(models.Model):
    #categories=[(str(c.name),c.name) for c in Category.objects.all() if c.parent is not None]
    name=models.CharField(max_length=100)
    descryption=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=100,unique=True)
    #category=models.CharField(max_length=100,choices=categories)
    category=models.ForeignKey(Category,related_name='product_category',on_delete=models.DO_NOTHING,null=True,blank=True)
                               #limit_choices_to=limit_category)
    price=models.FloatField(default=0.0)
    size=models.CharField(choices=[(s.size,s.size) for s in Size.objects.all()],max_length=10,blank=True,null=True)
    length=models.FloatField(default=0.0,blank=True,null=True)
    weight=models.FloatField(default=0.0,blank=True,null=True)

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
    def __str__(self):
        return f"{self.category}-{self.name}"
    def get_absolute_url(self):
        return reverse('product_front_detail_url',kwargs={'slug':self.slug})
    def get_update_url(self):
        return reverse('product_front_update_url',kwargs={'pk':self.id})
    def get_delete_url(self):
        return reverse('product_front_delete_url',kwargs={'pk':self.id})

