# Generated by Django 2.2.15 on 2020-08-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
