# Generated by Django 3.2.7 on 2021-09-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0010_uid_db_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersocialauth',
            name='access_token',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='usersocialauth',
            name='refresh_token',
            field=models.BinaryField(null=True),
        ),
    ]
