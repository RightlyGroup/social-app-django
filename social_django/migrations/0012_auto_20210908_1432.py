# Generated by Django 3.2.7 on 2021-09-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0011_auto_20210908_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersocialauth',
            name='access_token',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usersocialauth',
            name='refresh_token',
            field=models.TextField(null=True),
        ),
    ]
