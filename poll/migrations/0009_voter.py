# Generated by Django 3.0.1 on 2021-02-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_auto_20210224_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('votes', models.ManyToManyField(blank=True, related_name='voters', to='poll.Vote')),
            ],
        ),
    ]
