# Generated by Django 3.2.9 on 2022-03-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_pet_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=2),
        ),
    ]
