# Generated by Django 3.1.5 on 2022-03-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_usermodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]