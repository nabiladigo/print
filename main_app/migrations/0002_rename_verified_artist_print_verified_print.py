# Generated by Django 4.0.2 on 2022-02-09 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='print',
            old_name='verified_artist',
            new_name='verified_print',
        ),
    ]