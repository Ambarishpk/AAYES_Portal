# Generated by Django 4.1.4 on 2023-08-26 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aayesapp', '0004_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]