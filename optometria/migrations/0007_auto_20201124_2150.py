# Generated by Django 3.1.2 on 2020-11-25 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import optometria.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('optometria', '0006_auto_20201124_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hc',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hc_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pedido_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(verbose_name=optometria.models.Pedido.precio),
        ),
        migrations.AlterField(
            model_name='turno',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turno_medico', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turno_paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Medico',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]