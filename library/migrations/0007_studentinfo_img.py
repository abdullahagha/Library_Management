# Generated by Django 2.2.2 on 2019-11-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20191122_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
