# Generated by Django 4.2.1 on 2023-06-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_rename_data_inicio_historicoprofissional_data_ingresso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicoprofissional',
            name='data_ingresso',
            field=models.DateField(blank=True, max_length=100, null=True, verbose_name='data_inicio'),
        ),
    ]
