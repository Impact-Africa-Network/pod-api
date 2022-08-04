# Generated by Django 3.2.7 on 2021-09-19 14:52

from django.db import migrations, models
import ian_account.utils


class Migration(migrations.Migration):

    dependencies = [
        ('ian_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.jpeg', null=True, upload_to=ian_account.utils.user_avatar_directory),
        ),
    ]
