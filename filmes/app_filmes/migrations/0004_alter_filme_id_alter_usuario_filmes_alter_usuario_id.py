# Generated by Django 5.1.6 on 2025-03-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_filmes', '0003_rename_runtime_filme_ano_rename_year_filme_duracao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='filmes',
            field=models.ManyToManyField(blank=True, to='app_filmes.filme'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
