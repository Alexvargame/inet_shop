# Generated by Django 4.2.5 on 2023-12-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_last_name_order_name_remove_order_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
