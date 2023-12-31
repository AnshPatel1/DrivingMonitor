# Generated by Django 4.2.4 on 2023-11-05 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tracker', '0002_alter_locationhistory_latitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationhistory',
            options={'verbose_name': 'Location History', 'verbose_name_plural': 'Location History Timeline'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterModelOptions(
            name='trackernode',
            options={'verbose_name': 'Tracker Node', 'verbose_name_plural': 'Tracker Nodes'},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'verbose_name': 'Trip', 'verbose_name_plural': 'Trips'},
        ),
        migrations.AddField(
            model_name='locationhistory',
            name='city',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='locationhistory',
            name='country',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='locationhistory',
            name='region',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='organization',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TripEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('HARD_BRAKING', 'Hard Braking'), ('RAPID_ACCELERATION', 'Rapid Acceleration'), ('HARSH_LANE_CHANGE', 'Harsh Lane Change')], max_length=1024)),
                ('event_time', models.DateTimeField(auto_now=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracker.trip')),
            ],
            options={
                'verbose_name': 'Trip Event',
                'verbose_name_plural': 'Trip Events',
            },
        ),
    ]
