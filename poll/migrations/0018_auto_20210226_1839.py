# Generated by Django 3.0.1 on 2021-02-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0017_vote_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='poll.Voter'),
        ),
    ]