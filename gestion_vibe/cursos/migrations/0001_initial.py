# Generated by Django 5.2.1 on 2025-05-27 19:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('monto_cuota', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CPI',
                'verbose_name_plural': 'CPIs',
                'ordering': ['-fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fecha_inscripcion', models.DateField(default=django.utils.timezone.now)),
                ('activo', models.BooleanField(default=True)),
                ('cpi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alumnos', to='cursos.cpi')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
