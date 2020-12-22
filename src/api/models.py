from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField()
    description = models.TextField(default='Product Description.')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


class ProductItem(Product):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="+")
    size = models.CharField(max_length=2)
    price = models.PositiveBigIntegerField()  # store amount in paisa's or cents or whatever
    color = models.CharField(max_length=2)

    class Meta:
        db_table = 'product_item'


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    cart = models.ManyToManyField(ProductItem)


# Creating all django models
class Address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.PositiveIntegerField()

    class Meta:
        db_table = 'address'


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(ProductItem)

    class Meta:
        db_table = 'order'


# youtu.be/dQw4w9WgXcQ
