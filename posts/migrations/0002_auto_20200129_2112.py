# Generated by Django 2.1.15 on 2020-01-29 21:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likedone',
            field=models.ManyToManyField(related_name='users_video_main', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnumber',
            field=models.IntegerField(default=0, help_text='Начинается с 0', verbose_name='Число лайков'),
        ),
    ]