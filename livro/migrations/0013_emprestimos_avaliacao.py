# Generated by Django 4.0.3 on 2022-05-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_remove_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
