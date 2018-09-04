from django.db import models


class PeopleSays(models.Model):
    time = models.DateTimeField('发布时间', auto_now=True)
    name = models.CharField('用户名', default='No name', max_length=12)
    text = models.TextField('留言', default='no text', max_length=220)
    url = models.URLField('URL', null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
    class Meta:
        ordering = ['-time']

