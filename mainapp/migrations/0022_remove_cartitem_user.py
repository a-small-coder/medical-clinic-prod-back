# Generated by Django 3.2.5 on 2021-08-27 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20210825_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
