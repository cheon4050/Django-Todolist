# Generated by Django 3.2.13 on 2022-06-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0005_alter_todo_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
