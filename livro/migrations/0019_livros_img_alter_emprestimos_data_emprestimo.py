# Generated by Django 4.0.3 on 2022-06-14 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 9, 55, 53, 971287)),
        ),
    ]
