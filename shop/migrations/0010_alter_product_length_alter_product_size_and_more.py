# Generated by Django 4.2.5 on 2023-12-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[(1, '52'), (2, '50')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]