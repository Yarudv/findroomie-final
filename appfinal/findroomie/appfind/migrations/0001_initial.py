# Generated by Django 4.0.5 on 2022-07-06 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=35)),
                ('telefono', models.IntegerField(max_length=15)),
                ('direccion', models.CharField(max_length=35)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('clave', models.CharField(max_length=20)),
                ('confirmar_clave', models.CharField(max_length=20)),
            ],
        ),
    ]
