# Generated by Django 3.2.7 on 2021-09-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsApp', '0005_auto_20210917_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True),
        ),
    ]
