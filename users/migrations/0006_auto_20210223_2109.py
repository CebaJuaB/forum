# Generated by Django 3.0.1 on 2021-02-23 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210220_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='document',
            field=models.CharField(max_length=10),
        ),
    ]
