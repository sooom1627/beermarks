# Generated by Django 3.2 on 2021-05-23 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_drunk_postpic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drunk',
            name='postPic',
        ),
    ]
