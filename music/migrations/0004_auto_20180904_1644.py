# Generated by Django 2.1 on 2018-09-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_merge_20180904_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='author',
            field=models.TextField(max_length=50, verbose_name='创作者'),
        ),
    ]