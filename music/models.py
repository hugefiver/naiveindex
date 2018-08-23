from django.db import models

# Create your models here.


class Musics(models.Model):
    name = models.CharField('歌曲名称', max_length=50)
    author = models.TextField('创作者', max_length=50)
    pic = models.URLField('封面链接', null=True, blank=True)
    url = models.URLField('歌曲链接')

    def __str__(self):
        return self.name + ' - ' + self.author

