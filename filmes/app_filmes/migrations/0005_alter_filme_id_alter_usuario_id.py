# Generated by Django 5.1.6 on 2025-03-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_filmes', '0004_alter_filme_id_alter_usuario_filmes_alter_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
