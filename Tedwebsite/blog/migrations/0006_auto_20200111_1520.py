# Generated by Django 3.0.1 on 2020-01-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200111_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.TextField(default='https://medium.com/'),
        ),
    ]
