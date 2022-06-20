# Generated by Django 3.2.13 on 2022-06-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='finished',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo',
            field=models.CharField(default='', max_length=255),
        ),
    ]
