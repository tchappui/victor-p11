# Generated by Django 2.2.5 on 2019-09-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('substituter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stores',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
