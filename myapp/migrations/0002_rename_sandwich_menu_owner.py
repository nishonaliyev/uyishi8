# Generated by Django 4.2.7 on 2023-11-26 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='sandwich',
            new_name='owner',
        ),
    ]
