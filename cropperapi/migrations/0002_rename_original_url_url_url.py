# Generated by Django 3.2.6 on 2021-08-03 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cropperapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='original_url',
            new_name='url',
        ),
    ]