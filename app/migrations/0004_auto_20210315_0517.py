# Generated by Django 2.2.18 on 2021-03-15 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210315_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='r_content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='r_owner',
        ),
    ]
