from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)


#Django建议在首次迁移之前就定义好自定义用户模型
#如果先使用默认User模型创建了表和数据，再切换到自定义的模型会很麻烦