# Generated by Django 3.2.9 on 2021-11-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20211106_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
    ]