from django.db import models
from django.contrib.auth.models import User


class DiscontCard(models.Model):

    user=models.ForeignKey(User,related_name='user_discont',on_delete=models.DO_NOTHING)
    pension=models.BooleanField(default=False)
    accumulative=models.IntegerField(default=0)
    active=models.BooleanField(default=False)

    class Meta:
        verbose_name='Скидка'
        verbose_name_plural='Скидки'

    def __str__(self):
        return self.user.username
    #
    # def __dict__(self):
    #     return {'user':user.id,'pension':self.pension,'accumulative':self.accumulative}

