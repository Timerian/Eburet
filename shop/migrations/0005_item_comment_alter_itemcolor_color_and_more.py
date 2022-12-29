# Generated by Django 4.1.4 on 2022-12-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_itemcolor_options_alter_imageitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='itemcolor',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.color', verbose_name='Цвет предмета'),
        ),
        migrations.AlterField(
            model_name='itemcolor',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='shop.item', verbose_name='Предмет'),
        ),
    ]