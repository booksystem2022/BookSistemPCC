# Generated by Django 4.0.3 on 2022-05-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_alter_emprestimos_nome_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]