# Generated by Django 3.2.9 on 2022-03-03 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_petpost_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PetPostImages',
        ),
    ]
