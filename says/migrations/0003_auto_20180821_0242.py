# Generated by Django 2.0.7 on 2018-08-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('says', '0002_auto_20180818_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplesays',
            name='text',
            field=models.TextField(default='no text', max_length=220, verbose_name='留言'),
        ),
    ]
