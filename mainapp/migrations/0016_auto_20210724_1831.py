# Generated by Django 3.2.5 on 2021-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210724_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_key',
            field=models.CharField(default='12D@', max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('owner', 'session_key')},
        ),
    ]
