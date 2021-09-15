# Generated by Django 3.2.5 on 2021-08-25 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20210825_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Общая цена')),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='final_price',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_products',
        ),
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество товара'),
        ),
        migrations.DeleteModel(
            name='CartAnalyze',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='mainapp.cart', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Покупатель'),
        ),
    ]