# Generated by Django 4.0.2 on 2023-07-24 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_alter_match_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]