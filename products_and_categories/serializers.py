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
	
'''	def to_internal_value(self, data):
		try:
			try:
				obj_id = data['id']
				return Category.objects.get(id=obj_id)
			except KeyError:
				raise serializers.ValidationError(
					'id is a required field.'
				)
			except ValueError:
				raise serializers.ValidationError(
					'id must be an integer.'
				)
		except Category.DoesNotExist:
			raise serializers.ValidationError(
			'Obj does not exist.'
			)
'''
	
class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True)#, queryset= Category.objects.all(), slug_field='categories')
#	categories = CreatableSlugRelatedField(many=False,
#											queryset=Category.objects.all(),
#											slug_field='categories',
#											required=False)
	class Meta:
		model = Product
		fields = ('id', "product_code", "name", "quantity", "price", 'categories')

	def update(self, instance, validated_data):
		#category_data = validated_data.pop('categories')

		instance.product_code = validated_data.get('product_code', instance.product_code)
		instance.name = validated_data.get('name', instance.name)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)
		instance.categories = validated_data.get('categories', instance.categories)
		
		instance.save()
		return instance

	def create(self, validated_data):
		category_data = validated_data.get('categories')
		id_get = validated_data.get('id')
		id_pop = validated_data.pop('id')
		product = Product.objects.get_or_create(id=id_pop, **validated_data)
		for category in category_data:
			product.categories.get_or_create(**category)
		return product


