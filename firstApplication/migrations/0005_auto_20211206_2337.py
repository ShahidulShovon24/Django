# Generated by Django 3.2.9 on 2021-12-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApplication', '0004_auto_20211206_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='Address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='First_Admission_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='First_Name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='Last_Name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='cell',
            field=models.IntegerField(),
        ),
    ]
