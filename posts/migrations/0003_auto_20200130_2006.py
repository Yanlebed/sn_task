# Generated by Django 2.1.15 on 2020-01-30 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200129_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likedone',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnumber',
        ),
    ]
