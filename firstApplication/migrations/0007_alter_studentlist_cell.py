# Generated by Django 3.2.9 on 2021-12-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApplication', '0006_auto_20211207_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='cell',
            field=models.CharField(max_length=12),
        ),
    ]
