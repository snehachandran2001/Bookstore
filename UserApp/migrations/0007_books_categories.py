# Generated by Django 4.2.10 on 2024-02-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0006_rename_price_cart_cart_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='categories',
            field=models.CharField(max_length=255, null=True),
        ),
    ]