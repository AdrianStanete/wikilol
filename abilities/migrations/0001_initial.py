# Generated by Django 4.0.1 on 2022-01-15 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('champions', '0002_alter_champion_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.CharField(max_length=256, unique=True)),
                ('power', models.IntegerField()),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champions.champion')),
            ],
        ),
    ]
