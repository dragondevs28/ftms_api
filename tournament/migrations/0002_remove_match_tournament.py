# Generated by Django 4.0.2 on 2023-07-23 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='tournament',
        ),
    ]
