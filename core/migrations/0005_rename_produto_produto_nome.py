# Generated by Django 5.1.3 on 2024-11-11 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='produto',
            new_name='nome',
        ),
    ]
