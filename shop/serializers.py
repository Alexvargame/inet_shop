from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category,Product,Size

class CaregorySerializer(serializers.ModelSerializer):
    parent=serializers.URLField(max_length=200, min_length=None, allow_blank=False)

    class Meta:
        model=Category
        fields=('name','parent')

class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=('name','parent')

    def create(self, validated_data):
        category=Category.objects.update_or_create(
            name=validated_data.get('name',None)
        )
        return category

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model=Product
        fields=('name','category','price','size','length','weight','descryption')

class ProductCreateSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=[(s.id,s.size) for s in Size.objects.all()], style={'base_template': 'select.html'})
    length=serializers.FloatField(initial=0.0)
    weight = serializers.FloatField(initial=0.0)
    class Meta:
        model=Product
        fields=('name','category','slug','price','size','length','weight','descryption')

    def create(self, validated_data):
        product=Product.objects.update_or_create(
            name=validated_data.get('name',None),
            category=Category.objects.get(id=validated_data.get('category')),
            price=validated_data.get('price', None),
            size=validated_data.get('size', None),
            length=validated_data.get('length', None),
            weight=validated_data.get('weight', None),
            descryption=validated_data.get('descryption', None),
            slug=validated_data.get('slug',None),
        )
        return product

class ProductSearchSerializer(serializers.ModelSerializer):

    category = serializers.ChoiceField(choices=[(c.id,c.name) for c in Category.objects.all()], style={'base_template': 'select.html'})
    size = serializers.ChoiceField(choices=[(s.id,s.size) for s in Size.objects.all()], style={'base_template': 'radio.html'})

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'size', 'length', 'weight', 'descryption')

class OrderUserSerializer(serializers.Serializer):
    search_user=serializers.ChoiceField([(u.username,u.username) for u in User.objects.all()])