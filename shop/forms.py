from django import forms
from django.shortcuts import render, redirect
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

from django.forms import fields, widgets
from django.contrib.auth.models import User
from .models import Category,Product,Size

class ProductSearchForm(forms.Form):

    category = forms.CharField(label='Категория',
                               widget=forms.CheckboxSelectMultiple(
                                   choices=[(cat.id, cat.name) for cat in Category.objects.all()]))
    price_min=forms.FloatField(validators=[MinValueValidator(Decimal('0.0')),MaxValueValidator(Decimal('10000.0'))],
                               widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':10000}))
    price_max=forms.FloatField(validators=[MinValueValidator(Decimal('0.0')),MaxValueValidator(Decimal('10000.0'))],
                               widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':10000}))
    size= forms.CharField(label='Размер',
                               widget=forms.CheckboxSelectMultiple(
                                   choices=[(s.size, s.size) for s in Size.objects.all()]))
    # size_min=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    # size_max=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    length_min=forms.FloatField(
        widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':250}))
    length_max = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':250}))
    weight_min = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':200}))
    weight_max = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':200}))

class ProductSearchCategoryForm(forms.Form):
    category_lev_1 = Category.objects.filter(parent=None)
    category_lev_2 = Category.objects.filter(parent__in=category_lev_1)
    category_lev_3 = Category.objects.filter(parent__in=category_lev_2)
    category_1 = forms.CharField(label='Категория',
                               widget=forms.CheckboxSelectMultiple(
                                   choices=[(cat.id, cat.name) for cat in category_lev_1]))
    category_2 = forms.CharField(label='Подкатегория',
                                 widget=forms.CheckboxSelectMultiple(
                                     choices=[(cat.id, cat.name) for cat in category_lev_2]))
    category_3 = forms.CharField(label='Подкатегория',
                                 widget=forms.CheckboxSelectMultiple(
                                     choices=[(cat.id, cat.name) for cat in category_lev_3]))
    price_min=forms.FloatField(validators=[MinValueValidator(Decimal('0.0')),MaxValueValidator(Decimal('10000.0'))],
                               widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':10000}))
    price_max=forms.FloatField(validators=[MinValueValidator(Decimal('0.0')),MaxValueValidator(Decimal('10000.0'))],
                               widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':10000}))
    size= forms.CharField(label='Размер',
                               widget=forms.CheckboxSelectMultiple(
                                   choices=[(s.size, s.size) for s in Size.objects.all()]))
    # size_min=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    # size_max=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    length_min=forms.FloatField(
        widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True,'min':0.0,'max':250}))
    length_max = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':250}))
    weight_min = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':200}))
    weight_max = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True,'min':0.0,'max':200}))

class UserForm(forms.Form):
    search_user=forms.CharField(widget=forms.Select(choices=[(u.username,u.username) for u in User.objects.all()]))







