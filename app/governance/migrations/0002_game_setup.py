# Generated by Django 2.2.4 on 2020-09-26 03:33

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='setup',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]