# Generated by Django 4.2.1 on 2023-05-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cor_ou_raca',
            field=models.CharField(choices=[('Amarela', 'Amarela'), ('Branca', 'Branca'), ('Indígena', 'Indígena'), ('Parda', 'Parda'), ('Preta', 'Preta'), ('Prefiro não informar', 'Prefiro não informar'), ('Outra', 'Outra')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro não informar', 'Prefiro não informar'), ('Outro', 'Outro')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nome_exibicao',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='outra_cor_ou_raca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='outro_genero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rg',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nome_completo',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
