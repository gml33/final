# Generated by Django 3.1.2 on 2020-12-02 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0003_lente_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lente',
            name='pedido',
        ),
    ]