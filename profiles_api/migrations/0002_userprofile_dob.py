# Generated by Django 2.2 on 2022-03-14 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
