# Generated by Django 3.1.4 on 2020-12-16 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201216_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-upload_date']},
        ),
    ]