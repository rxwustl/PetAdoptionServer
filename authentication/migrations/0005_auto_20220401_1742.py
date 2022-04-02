# Generated by Django 3.2.9 on 2022-04-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20220304_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='addressLine',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='longitude'),
        ),
    ]