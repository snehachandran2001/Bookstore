# Generated by Django 4.2.10 on 2024-02-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
