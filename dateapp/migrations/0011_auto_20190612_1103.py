# Generated by Django 2.2.1 on 2019-06-12 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dateapp', '0010_remove_spot_name_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='like',
        ),
        migrations.AddField(
            model_name='spot',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
