# Generated by Django 4.0.2 on 2023-07-25 17:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_alter_match_date'),
        ('knockout', '0012_qualifyteam_sf_loser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifyteam',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.group'),
        ),
        migrations.CreateModel(
            name='RoundOf32',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('team1_score', models.PositiveIntegerField(blank=True, null=True)),
                ('team2_score', models.PositiveIntegerField(blank=True, null=True)),
                ('is_match_ended', models.BooleanField(default=False)),
                ('position', models.PositiveIntegerField(blank=True, null=True)),
                ('team1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='round_of_32_team1', to='knockout.qualifyteam')),
                ('team2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='round_of_32_team2', to='knockout.qualifyteam')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.mytournament')),
            ],
        ),
    ]