# Generated by Django 3.1.4 on 2020-12-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='buyer_rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='seller_rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
