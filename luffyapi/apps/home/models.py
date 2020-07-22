from django.db import models
from utils.model import BaseModel


class Banner(BaseModel):
    name = models.CharField(max_length=16, verbose_name='图片名字')
    img = models.ImageField(upload_to='banner', verbose_name='轮播图图片', help_text='尺寸为3840*800')
    link = models.CharField(max_length=64, verbose_name='跳转链接')
    info = models.TextField(verbose_name='图片描述')




