# Generated by Django 4.0.3 on 2022-03-20 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendaciones', '0002_rename_documentales_documental_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Serie',
            new_name='Documentales',
        ),
        migrations.RenameModel(
            old_name='Documental',
            new_name='Peliculas',
        ),
        migrations.RenameModel(
            old_name='Pelicula',
            new_name='Series',
        ),
    ]
