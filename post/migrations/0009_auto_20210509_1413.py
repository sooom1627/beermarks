# Generated by Django 3.2 on 2021-05-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20210413_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drunk',
            name='com',
            field=models.TextField(blank=True, default='記録用(Just for recording)', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='drunk',
            name='rate',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
    ]
