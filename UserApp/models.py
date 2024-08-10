from django.db import models
from django.db import models


class USERDATA(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'userdatas'


class BOOKS(models.Model):
    coverimg = models.ImageField(upload_to='images/')
    bookname = models.CharField(max_length=255)
    authorname = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    categories = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    publication_date = models.DateField(null=True)

    class Meta:
        db_table = 'booksdata'

    def __str__(self):
        return self.bookname


class CART(models.Model):
    user = models.ForeignKey(USERDATA, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(BOOKS, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()

    class Meta:
        db_table = 'cartdata'


class REVIEWS(models.Model):
    user = models.ForeignKey(USERDATA, on_delete=models.CASCADE)
    book = models.ForeignKey(BOOKS, on_delete=models.CASCADE, null=True)
    review = models.TextField(max_length=500)
    star = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviewsdata'
