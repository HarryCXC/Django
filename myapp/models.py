from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')


class Group(models.Model):
    group_name = models.CharField(max_length=32, verbose_name='团体名称')
    group_script = models.CharField(max_length=60, verbose_name='备注')

    def __str__(self):
        return self.user
