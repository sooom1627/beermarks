# Generated by Django 3.2 on 2021-05-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_remove_drunk_postpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='drunk',
            name='postPic',
            field=models.ImageField(null=True, upload_to='images/post'),
        ),
    ]