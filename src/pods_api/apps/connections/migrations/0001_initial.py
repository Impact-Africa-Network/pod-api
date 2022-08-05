# Generated by Django 4.1 on 2022-08-05 05:09

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('ld_number', models.CharField(max_length=10, unique=True)),
                ('person_met', models.CharField(max_length=255)),
                ('date_met', models.DateField()),
                ('meeting_details', models.CharField(max_length=500)),
                ('fun_fact', models.CharField(max_length=500)),
                ('points', models.IntegerField(max_length=100)),
            ],
            options={
                'ordering': [builtins.id],
            },
        ),
    ]