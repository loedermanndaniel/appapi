# Generated by Django 5.0.1 on 2024-01-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
