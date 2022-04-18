# Generated by Django 3.2.9 on 2022-04-18 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20220418_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pref_user', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
