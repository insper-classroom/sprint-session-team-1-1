# Generated by Django 4.2.1 on 2023-05-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_cor_ou_raca_profile_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cor_ou_raca',
            field=models.CharField(choices=[('Amarela', 'Amarela'), ('Branca', 'Branca'), ('Indígena', 'Indígena'), ('Parda', 'Parda'), ('Preta', 'Preta'), ('Prefiro não informar', 'Prefiro não informar'), ('Outra', 'Outra')], max_length=20, null=True, verbose_name='Cor ou Raça'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='data_nascimento',
            field=models.DateField(null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro não informar', 'Prefiro não informar'), ('Outro', 'Outro')], max_length=20, null=True, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nome_completo',
            field=models.CharField(max_length=150, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nome_exibicao',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome de exibição'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='outra_cor_ou_raca',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Outra'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='outro_genero',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Outro'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rg',
            field=models.CharField(max_length=12, null=True, verbose_name='RG'),
        ),
    ]
