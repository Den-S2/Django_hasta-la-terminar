# Generated by Django 4.1.4 on 2023-01-17 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finaltraininng', '0004_alter_abon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abon',
            name='Name',
        ),
    ]
