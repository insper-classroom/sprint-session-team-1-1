# Generated by Django 4.2.1 on 2023-05-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_nome_completo_profile_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ano_formatura',
            field=models.CharField(max_length=4, null=True, verbose_name='Ano de Formatura'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ano_ingresso',
            field=models.CharField(max_length=4, null=True, verbose_name='Ano de Ingresso'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cidade_atual',
            field=models.CharField(blank=True, choices=[('china', 'china'), ('India', 'India'), ('hong kong', 'hong kong')], max_length=100, null=True, verbose_name='Cidade Atual'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cidade_nascimento',
            field=models.CharField(blank=True, choices=[('china', 'china'), ('India', 'India'), ('hong kong', 'hong kong')], max_length=100, null=True, verbose_name='Cidade de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_atual',
            field=models.CharField(blank=True, choices=[('china', 'china'), ('India', 'India'), ('hong kong', 'hong kong')], max_length=100, null=True, verbose_name='Estado Atual'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_nascimento',
            field=models.CharField(blank=True, choices=[('china', 'china'), ('India', 'India'), ('hong kong', 'hong kong')], max_length=100, null=True, verbose_name='Estado de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pais_atual',
            field=models.CharField(blank=True, choices=[('china', 'china'), ('India', 'India'), ('hong kong', 'hong kong')], max_length=100, null=True, verbose_name='País Atual'),
        ),
    ]
