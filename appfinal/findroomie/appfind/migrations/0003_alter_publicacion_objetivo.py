# Generated by Django 4.0.5 on 2022-07-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfind', '0002_publicacion_delete_registrousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='objetivo',
            field=models.BooleanField(choices=[(True, 'Compartir tu hogar'), (False, 'Buscar un lugar')]),
        ),
    ]