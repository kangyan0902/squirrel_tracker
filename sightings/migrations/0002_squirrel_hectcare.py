# Generated by Django 3.0 on 2019-12-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='Hectcare',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
