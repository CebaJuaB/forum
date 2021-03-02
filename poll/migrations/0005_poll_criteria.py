# Generated by Django 3.0.1 on 2021-02-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_poll_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='criteria',
            field=models.CharField(choices=[('IN', 'Individual'), ('CO', 'Coeficiente'), ('SH', 'Acciones')], default='CO', max_length=2),
        ),
    ]