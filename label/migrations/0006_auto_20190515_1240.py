# Generated by Django 2.0.5 on 2019-05-15 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0005_catagorys_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelitem',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='标记时间'),
        ),
    ]