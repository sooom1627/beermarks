# Generated by Django 3.2 on 2021-04-29 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_upic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='udesc',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]