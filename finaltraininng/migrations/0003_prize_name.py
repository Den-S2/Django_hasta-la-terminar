# Generated by Django 4.1.4 on 2023-01-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltraininng', '0002_trainer_surname_alter_trainer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
