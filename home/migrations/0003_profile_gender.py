# Generated by Django 3.2 on 2021-05-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_users_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='man', max_length=64),
            preserve_default=False,
        ),
    ]
