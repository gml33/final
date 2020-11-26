# Generated by Django 3.1.2 on 2020-11-26 23:26

from django.db import migrations, models
import optometria.models


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0013_auto_20201126_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(verbose_name=optometria.models.Pedido.precio),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateField(),
        ),
    ]