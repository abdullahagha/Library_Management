# Generated by Django 2.2 on 2020-06-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
