# Generated by Django 2.0.7 on 2018-08-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('says', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peoplesays',
            options={'ordering': ['-time']},
        ),
        migrations.RemoveField(
            model_name='peoplesays',
            name='date',
        ),
        migrations.AddField(
            model_name='peoplesays',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='peoplesays',
            name='name',
            field=models.TextField(default='No name', max_length=12, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='peoplesays',
            name='text',
            field=models.TextField(default='no text', max_length=120, verbose_name='留言'),
        ),
        migrations.AlterField(
            model_name='peoplesays',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
    ]
