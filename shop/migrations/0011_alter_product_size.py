# Generated by Django 4.2.5 on 2023-12-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_product_length_alter_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('52', '52'), ('50', '50')], max_length=10, null=True),
        ),
    ]
