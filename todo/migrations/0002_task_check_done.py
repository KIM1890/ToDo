# Generated by Django 4.0 on 2021-12-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='check_done',
            field=models.BooleanField(null=True),
        ),
    ]