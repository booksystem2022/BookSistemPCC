# Generated by Django 4.0.3 on 2022-05-07 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0005_categoria_livros_usuario_livros_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
