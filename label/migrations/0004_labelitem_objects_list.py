# Generated by Django 2.0.5 on 2019-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0003_labelrecord_has_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelitem',
            name='objects_list',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='包含对象'),
        ),
    ]
