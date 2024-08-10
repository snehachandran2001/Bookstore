from django.db import models

# Create your models here.

class BookStore(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    book_description=models.TextField()
    book_image=models.ImageField(upload_to='media')


    class Meta:
        db_table = 'bookstore'

    def __str__(self):
        return self.book_name

class UserDetails(models.Model):
    user_name=models.CharField(max_length=100)
    user_password=models.CharField(max_length=10)
    user_number=models.CharField(max_length=10)
    user_image=models.ImageField(upload_to='media')


    class Meta:
        db_table = 'userdetails'

    def __str__(self):
        return self.user_name
