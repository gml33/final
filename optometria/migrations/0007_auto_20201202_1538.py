# Generated by Django 3.1.2 on 2020-12-02 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('optometria', '0006_lente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(default=18, on_delete=django.db.models.deletion.CASCADE, related_name='pedido_vendedor', to='user.user'),
            preserve_default=False,
        ),
    ]