# Generated by Django 3.2 on 2021-05-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_udesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uname',
            field=models.CharField(blank=True, default='noname', max_length=50),
        ),
    ]