# Generated by Django 4.2.10 on 2024-02-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_userdata_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverimg', models.ImageField(upload_to='images/')),
                ('bookname', models.CharField(max_length=255)),
                ('authorname', models.CharField(max_length=255)),
                ('availability', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'booksdata',
            },
        ),
    ]
