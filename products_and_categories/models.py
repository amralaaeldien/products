from django.db import models

# Create your models here.

class Category(models.Model):
	#id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	categoriesId = models.ForeignKey('self', related_name='categories',on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	#id = models.PositiveIntegerField(primary_key=True)
	product_code = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	quantity = models.IntegerField()
	categories = models.ManyToManyField(Category, related_name='products')
	
	def __str__(self):
		return self.name

