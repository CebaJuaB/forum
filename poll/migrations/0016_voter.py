# Generated by Django 3.0.1 on 2021-02-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0015_auto_20210226_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
            ],
        ),
    ]