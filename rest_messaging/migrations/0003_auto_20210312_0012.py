# Generated by Django 3.1.7 on 2021-03-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_messaging', '0002_auto_20210311_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]