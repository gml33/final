# Generated by Django 3.1.2 on 2020-12-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optometria', '0005_delete_lente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia', models.CharField(choices=[('cerca', 'Cerca'), ('lejos', 'Lejos')], default='cerca', max_length=16)),
                ('lado', models.CharField(choices=[('izquierdo', 'Izquierdo'), ('derecho', 'Derecho')], default='izquierdo', max_length=16)),
                ('armazon', models.BooleanField(default=False)),
                ('precio', models.FloatField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lente_pedido', to='optometria.pedido')),
            ],
        ),
    ]
