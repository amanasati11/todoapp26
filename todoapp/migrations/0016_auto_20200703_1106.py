# Generated by Django 2.0 on 2020-07-03 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0015_userprofile_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usertype',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]