# Generated by Django 4.1.4 on 2023-01-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltraininng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='Surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
