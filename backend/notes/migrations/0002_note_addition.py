# Generated by Django 2.1.7 on 2019-03-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='addition',
            field=models.TextField(default=''),
        ),
    ]