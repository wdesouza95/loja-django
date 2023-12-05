# Generated by Django 4.2.7 on 2023-12-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_banner_remove_product_price_productattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/cat_imgs/'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='image',
            field=models.ImageField(upload_to='media/marca_imgs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/product_imgs/'),
        ),
    ]
