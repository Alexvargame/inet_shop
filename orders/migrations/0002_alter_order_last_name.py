# Generated by Django 4.2.5 on 2023-12-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]