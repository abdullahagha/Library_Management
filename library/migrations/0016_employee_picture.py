# Generated by Django 2.2 on 2020-06-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20200604_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
