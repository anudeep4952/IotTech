# Generated by Django 2.1.7 on 2019-03-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='userid',
            field=models.CharField(blank=True, default='y16it832', max_length=255),
        ),
    ]