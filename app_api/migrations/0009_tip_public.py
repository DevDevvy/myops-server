# Generated by Django 4.0.5 on 2022-06-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0008_journal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]