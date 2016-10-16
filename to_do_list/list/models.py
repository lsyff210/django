from django.db import models

# Create your models here.


class todo_list(models.Model):
    thing = models.CharField(max_length=200, verbose_name="待做的事情")
    state = models.BooleanField(max_length=1, choices=((0, '待做'), (1, '完成'),), default=0)
