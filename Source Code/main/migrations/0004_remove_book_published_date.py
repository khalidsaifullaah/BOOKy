# Generated by Django 3.1.4 on 2020-12-16 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201216_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
    ]
