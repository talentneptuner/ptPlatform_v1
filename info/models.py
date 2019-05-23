from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    mid = models.CharField(max_length=50, verbose_name='绑定id')
    img_name = models.CharField(max_length=50, verbose_name='文件名')

    class Meta:
        managed = False
        db_table = 'image'
        verbose_name = '图片'
        verbose_name_plural = '图片'


class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    mid = models.CharField(max_length=40, verbose_name='绑定id')
    text = models.TextField(verbose_name='文本')

    class Meta:
        managed = False
        db_table = 'text'
        verbose_name = '文本'
        verbose_name_plural = verbose_name


