# Generated by Django 2.1.3 on 2018-11-21 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_and_categories', '0002_auto_20181121_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categoriesId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products_and_categories.Category'),
        ),
    ]