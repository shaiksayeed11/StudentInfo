# Generated by Django 3.2.11 on 2022-01-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='studentrollno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
