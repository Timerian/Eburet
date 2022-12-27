# Generated by Django 4.1.4 on 2022-12-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_item_vendor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='concept',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Концепт'),
        ),
        migrations.AddField(
            model_name='item',
            name='production_time',
            field=models.CharField(blank=True, max_length=150, verbose_name='Время изготовления'),
        ),
    ]