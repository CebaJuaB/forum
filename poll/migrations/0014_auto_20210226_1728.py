# Generated by Django 3.0.1 on 2021-02-26 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0013_remove_vote_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='poll.Poll'),
        ),
    ]