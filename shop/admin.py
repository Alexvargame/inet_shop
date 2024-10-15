from django.contrib import admin
from django import forms

from .models import Category,Product,Size

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent')

class CategoryChoiceForm(forms.ModelForm):
    #category=forms.CharField(widget=forms.ChoiceField(Category.objects.filter(parent__isnull=False)))
    class Meta:
        model=Product
        fields=['name','category']

    def __init__(self, *args, **kwargs):
        super(CategoryChoiceForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(parent__isnull=False)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id','size')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product', {'fields': ['name','slug','category','price','size','length','weight','descryption']}),
    ]
    list_display = ('id','name','category','price','size','length','weight','descryption')
    form=CategoryChoiceForm