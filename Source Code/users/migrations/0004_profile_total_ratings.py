# Generated by Django 3.1.4 on 2021-01-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201215_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_ratings',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
