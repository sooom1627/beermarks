# Generated by Django 3.2 on 2021-04-28 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_brand_bname_search_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='bdesc',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_n', to='product.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
