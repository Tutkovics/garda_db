# Generated by Django 3.0.5 on 2020-04-19 16:53

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
