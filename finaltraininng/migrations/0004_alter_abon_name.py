# Generated by Django 4.1.4 on 2023-01-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltraininng', '0003_prize_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abon',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]