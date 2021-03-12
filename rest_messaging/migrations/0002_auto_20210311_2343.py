# Generated by Django 3.1.7 on 2021-03-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='text_body',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
