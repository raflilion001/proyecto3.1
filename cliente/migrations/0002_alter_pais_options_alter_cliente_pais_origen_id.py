# Generated by Django 5.0.1 on 2024-01-11 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'país', 'verbose_name_plural': 'países'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.pais', verbose_name='país de origen'),
        ),
    ]
