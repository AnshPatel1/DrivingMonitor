# Generated by Django 4.2.4 on 2023-11-05 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_trip_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationhistory',
            name='trip',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tracker.trip'),
        ),
    ]
