from django.db import models
from users.models import UserProfile
from info.models import Image, Text

from datetime import datetime


# Create your models here.

class CatagoryF(models.Model):
    name = models.CharField(max_length=30, verbose_name='标记名')

    def get_sub_cat(self):
        return self.catagorys_set.all()

    class Meta:
        verbose_name = '一类标记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CatagoryS(models.Model):
    name = models.CharField(max_length=30, verbose_name='标记名')
    catagory_f = models.ForeignKey(CatagoryF, verbose_name='一级类别', on_delete=models.CASCADE)
    desc = models.CharField(max_length=500, verbose_name='说明', blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '二级类别'
        verbose_name = '二级类别'

class labelRecord(models.Model):
    recorder = models.ForeignKey(UserProfile, verbose_name='标记人', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, verbose_name='图片', on_delete=models.CASCADE)
    text = models.ForeignKey(Text, verbose_name='文本', on_delete=models.CASCADE)
    has_done = models.BooleanField(default=False)



class labelitem(models.Model):
    recorder = models.ForeignKey(UserProfile, verbose_name='标记人', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='image')
    mid = models.CharField(max_length=100, verbose_name='微博id')
    text = models.TextField(verbose_name='文本')
    time = models.DateTimeField(verbose_name='标记时间', default=datetime.now)
    cat_id = models.ForeignKey(CatagoryS, verbose_name='类别', on_delete=models.CASCADE, blank=True, null=True)
    objects_list = models.CharField(verbose_name='包含对象', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '标记记录'
        verbose_name_plural = '标记记录'




