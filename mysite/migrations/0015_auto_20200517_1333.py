# Generated by Django 3.0.4 on 2020-05-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20200517_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitstop',
            name='link',
            field=models.URLField(default='#'),
        ),
    ]