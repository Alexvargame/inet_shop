# Generated by Django 4.2.5 on 2023-12-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(2, 'Куртка'), (3, 'Пуховик')], max_length=100),
        ),
    ]