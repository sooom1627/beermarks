# Generated by Django 3.2 on 2021-05-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210528_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medium',
            name='ecsite',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='facebook',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='instagram',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='twitter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='website',
            field=models.TextField(blank=True, null=True),
        ),
    ]
