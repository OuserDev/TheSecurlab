# Generated by Django 4.2.4 on 2023-08-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_remove_post_thumbnailimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='notice_id',
        ),
        migrations.AddField(
            model_name='post',
            name='group_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='분류'),
        ),
    ]
