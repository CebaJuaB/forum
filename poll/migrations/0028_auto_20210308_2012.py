# Generated by Django 3.0.1 on 2021-03-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0027_auto_20210305_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='coeficient',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]