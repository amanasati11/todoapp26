# Generated by Django 2.0 on 2020-07-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0016_auto_20200703_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
