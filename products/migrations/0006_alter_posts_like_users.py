# Generated by Django 4.2 on 2024-04-18 16:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_posts_image_posts_like_users_alter_posts_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
