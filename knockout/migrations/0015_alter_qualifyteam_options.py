# Generated by Django 4.0.2 on 2023-07-28 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knockout', '0014_rename_final_winner_qualifyteam_champion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qualifyteam',
            options={'ordering': ['-champion', '-sfw', '-tpw', '-qfw']},
        ),
    ]
