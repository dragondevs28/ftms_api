# Generated by Django 4.0.2 on 2023-07-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_match_is_statistics_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytournament',
            name='current_stage',
            field=models.CharField(choices=[('Group', 'Group Stage'), ('Round32', 'Round of 32'), ('Round16', 'Round of 16'), ('QuarterFinal', 'Quarter Final'), ('SemiFinal', 'Semi Final'), ('Final', 'Final')], default='Group', max_length=20),
        ),
        migrations.AlterField(
            model_name='mytournament',
            name='teams_selection',
            field=models.CharField(choices=[('4', 4), ('8', 8), ('16', 16), ('32', 32), ('64', 64)], max_length=2),
        ),
    ]
