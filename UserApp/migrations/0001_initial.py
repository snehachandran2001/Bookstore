# Generated by Django 4.2.10 on 2024-02-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USERDATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]