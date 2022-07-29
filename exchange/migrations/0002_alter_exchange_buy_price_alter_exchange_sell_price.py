# Generated by Django 4.0.4 on 2022-05-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='buy_price',
            field=models.DecimalField(decimal_places=5, max_digits=19),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='sell_price',
            field=models.DecimalField(decimal_places=5, max_digits=19),
        ),
    ]
