# Generated by Django 4.2.1 on 2023-05-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_cidade_atual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cidade_atual',
            field=models.CharField(blank=True, choices=[('hong kong', 'hong kong'), ('china', 'china'), ('India', 'India')], max_length=100, null=True, verbose_name='Cidade Atual'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cidade_nascimento',
            field=models.CharField(blank=True, choices=[('hong kong', 'hong kong'), ('china', 'china'), ('India', 'India')], max_length=100, null=True, verbose_name='Cidade de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_atual',
            field=models.CharField(blank=True, choices=[('hong kong', 'hong kong'), ('china', 'china'), ('India', 'India')], max_length=100, null=True, verbose_name='Estado Atual'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_nascimento',
            field=models.CharField(blank=True, choices=[('hong kong', 'hong kong'), ('china', 'china'), ('India', 'India')], max_length=100, null=True, verbose_name='Estado de Nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pais_atual',
            field=models.CharField(blank=True, choices=[('hong kong', 'hong kong'), ('china', 'china'), ('India', 'India')], max_length=100, null=True, verbose_name='País Atual'),
        ),
    ]
