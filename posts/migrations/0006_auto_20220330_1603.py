# Generated by Django 3.2.9 on 2022-03-30 16:03

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220329_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='petpost',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=posts.models.upload_to, verbose_name='Image'),
        ),
        migrations.DeleteModel(
            name='PetPostImages',
        ),
    ]