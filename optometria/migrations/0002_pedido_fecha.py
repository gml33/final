# Generated by Django 3.1.2 on 2020-11-27 16:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 27, 16, 1, 58, 391447, tzinfo=utc)),
            preserve_default=False,
        ),
    ]