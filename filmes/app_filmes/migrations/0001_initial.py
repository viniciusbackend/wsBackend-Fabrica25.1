# Generated by Django 5.1.6 on 2025-03-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('runtime', models.IntegerField(max_length=3)),
                ('diretor', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
    ]
