# Generated by Django 3.1.4 on 2020-12-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201216_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='book_covers'),
        ),
    ]
