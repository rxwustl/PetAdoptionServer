# Generated by Django 3.2.9 on 2022-04-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_userpreference_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreference',
            name='breed',
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='age',
            field=models.CharField(default='N', max_length=4),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='pettype',
            field=models.CharField(default='N', max_length=4),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='weight',
            field=models.CharField(default='N', max_length=4),
        ),
    ]
