# Generated by Django 3.2.9 on 2022-04-18 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_user_profilephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pettype', models.CharField(default='CAT', max_length=4)),
                ('age', models.IntegerField(default=1)),
                ('breed', models.CharField(default='', max_length=64)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pref_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
