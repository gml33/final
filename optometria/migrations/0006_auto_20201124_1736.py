# Generated by Django 3.1.2 on 2020-11-24 20:36

from django.db import migrations, models
import optometria.models


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0005_auto_20201124_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(verbose_name=optometria.models.Pedido.precio),
        ),
    ]
