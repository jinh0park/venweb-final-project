# Generated by Django 2.2.1 on 2019-06-11 02:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dateapp', '0004_remove_spot_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='like',
        ),
        migrations.AddField(
            model_name='spot',
            name='like',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
