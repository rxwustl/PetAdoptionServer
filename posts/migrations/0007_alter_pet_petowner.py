# Generated by Django 3.2.9 on 2022-04-01 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20220330_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='petowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petowner', to=settings.AUTH_USER_MODEL),
        ),
    ]
