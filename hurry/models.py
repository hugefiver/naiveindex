from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=20, default='')
    create_date = models.DateField('CreateDate', auto_now_add=True)
    change_date = models.DateField('ChangeDate', auto_now=True)
    main_text = models.TextField('MainText')


class PinPost(models.Model):
    title = models.CharField('Title', max_length=20, default='')
    pin = models.IntegerField('Pin', default=1)
    create_date = models.DateField('CreateDate', auto_now_add=True)
    change_date = models.DateField('ChangeDate', auto_now=True)
    main_text = models.TextField('MainText')

