# Generated by Django 3.0.6 on 2020-05-21 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200521_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languagestools',
            old_name='item',
            new_name='name',
        ),
    ]
