# Generated by Django 3.2.11 on 2022-01-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiving_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='copies',
            field=models.IntegerField(default=0),
        ),
    ]
