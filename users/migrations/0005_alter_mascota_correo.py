# Generated by Django 4.0.4 on 2022-05-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_juguete_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='correo',
            field=models.EmailField(max_length=50, verbose_name='correo de contacto'),
        ),
    ]
