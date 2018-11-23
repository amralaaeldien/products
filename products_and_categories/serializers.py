from rest_framework import serializers
from products_and_categories.models import Product, Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', "name", 'products', 'categories')
	
	def to_representation(self, obj):
		if 'categories' not in self.fields:
			self.fields['categories'] = CategorySerializer(obj, many=True)      
		return super(CategorySerializer, self).to_representation(obj)

	
class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True)

	class Meta:
		model = Product
		fields = ('id', "product_code", "name", "quantity", "price", 'categories')

	def update(self, instance, validated_data):

		instance.product_code = validated_data.get('product_code', instance.product_code)
		instance.name = validated_data.get('name', instance.name)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)
		instance.categories = validated_data.get('categories', instance.categories)
		
		instance.save()
		return instance

	def create(self, validated_data):
		category_data = validated_data.get('categories')
		product = Product.objects.create(**validated_data)
		for category in category_data:
			product.categories.create(**category)
		return product


