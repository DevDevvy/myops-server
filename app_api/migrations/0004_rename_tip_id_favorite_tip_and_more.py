# Generated by Django 4.0.5 on 2022-06-08 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_rename_tip_favorite_tip_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='tip_id',
            new_name='tip',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='user_id',
            new_name='user',
        ),
    ]
