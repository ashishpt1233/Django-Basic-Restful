# Generated by Django 3.0 on 2020-01-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(max_length=100),
        ),
    ]
