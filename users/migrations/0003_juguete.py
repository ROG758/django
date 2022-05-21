# Generated by Django 4.0.4 on 2022-05-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='juguete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, verbose_name='tipo de juguete')),
                ('descripcion', models.TextField(verbose_name='Descripcion de juegute')),
                ('compra', models.DateField(auto_now=True, verbose_name='fecha de compra')),
            ],
        ),
    ]
