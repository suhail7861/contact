# Generated by Django 3.2.4 on 2021-09-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(default='number', max_length=10),
        ),
    ]
