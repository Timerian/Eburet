# Generated by Django 4.1.4 on 2022-12-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_imageitem_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='equipment',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Комплектация'),
        ),
    ]
