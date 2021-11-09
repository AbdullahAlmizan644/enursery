from django.db import models

# Create your models here.

class Shop(models.Model):
	shopName=models.CharField(max_length=200)
	shopImage = models.CharField(max_length=100)

	def __str__(self):
		return self.shopName

class Post(models.Model):
	productName=models.CharField(max_length=200)

	productDescription=models.CharField(max_length=2000)

	productImage=models.CharField(max_length=200)

	productPrice=models.CharField(max_length=200)

	shopName = models.ForeignKey(Shop, on_delete=models.CASCADE)

	category=models.CharField(max_length=200)

	date=models.DateField()


	def __str__(self):
		return self.productName



