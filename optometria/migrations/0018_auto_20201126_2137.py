# Generated by Django 3.1.2 on 2020-11-27 00:37

from django.db import migrations, models
import optometria.models


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0017_auto_20201126_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hc',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(verbose_name=optometria.models.Pedido.precio),
        ),
    ]
