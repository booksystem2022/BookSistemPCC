# Generated by Django 4.0.3 on 2022-05-09 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_alter_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='tempo_duracao',
        ),
    ]