# Generated by Django 2.1.5 on 2019-06-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dateapp', '0003_auto_20190604_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='location',
        ),
    ]
