# Generated by Django 4.0.3 on 2022-06-14 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_livros_img_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='avaliacao',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 16, 27, 15, 235126)),
        ),
    ]
