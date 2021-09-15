# Generated by Django 3.2.5 on 2021-08-30 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_done',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата завершения (автоматически)'),
        ),
    ]