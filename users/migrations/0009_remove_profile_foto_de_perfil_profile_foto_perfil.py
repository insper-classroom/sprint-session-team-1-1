# Generated by Django 4.2.1 on 2023-05-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_foto_de_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='foto_de_perfil',
        ),
        migrations.AddField(
            model_name='profile',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='sprint/static/profile_img', verbose_name='Foto de Perfil'),
        ),
    ]
