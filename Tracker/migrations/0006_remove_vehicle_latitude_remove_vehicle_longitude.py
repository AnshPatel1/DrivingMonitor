# Generated by Django 4.2.4 on 2023-11-05 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0005_alter_trackernode_node_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='longitude',
        ),
    ]
