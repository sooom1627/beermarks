# Generated by Django 3.2 on 2021-05-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_drunk_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drunk',
            name='postPic',
            field=models.ImageField(default='images/post/noimage.png', upload_to='images/post'),
        ),
    ]