# Generated by Django 3.2.11 on 2022-04-16 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods_container', '0002_container_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 22, 53, 44, 603138)),
        ),
        migrations.AddField(
            model_name='container',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 22, 53, 44, 603162)),
        ),
        migrations.AlterField(
            model_name='container',
            name='name',
            field=models.CharField(max_length=50, verbose_name='container name'),
        ),
    ]
