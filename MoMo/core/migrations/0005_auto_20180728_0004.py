# Generated by Django 2.0.7 on 2018-07-28 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pspadapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pspadapter',
            name='port',
            field=models.IntegerField(null=True),
        ),
    ]