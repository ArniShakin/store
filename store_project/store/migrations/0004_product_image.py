# Generated by Django 4.2.3 on 2023-09-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/607180-chevrolet-camaro-ss-car-auto-motors.jpg', upload_to='images/'),
        ),
    ]
