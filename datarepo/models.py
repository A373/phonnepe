from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    phone = models.BigIntegerField(unique=True, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name_plural = 'users'


class Operators(models.Model):
    OPERATOR_TYPES = [
        ('Airtel', 'Airtel'),
        ('IDEA', 'IDEA'),
        ('JIO', 'JIO'),
        ('BSNL', 'BSNL')
    ]

    operator_name = models.CharField(max_length=255, choices=OPERATOR_TYPES)

    def __str__(self):
        return str(self.operator_name)

    class Meta:
        verbose_name_plural = 'operators'


class Plans(models.Model):
    VIEW_PLANS = [
        ('SMS', 'SMS'),
        ('DATA', 'DATA'),
        ('TALK Time', 'TALK TIME')

    ]
    plans = models.CharField(max_length=255, choices=VIEW_PLANS)

    def __str__(self):
        return str(self.plans)

    class Meta:
        verbose_name_plural = 'plans'


class Recharge(models.Model):
    phone_number = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    operator_name = models.ForeignKey(Operators, on_delete=models.SET_NULL, null=True, blank=True)
    view_plan = models.ForeignKey(Plans, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField()
    validity = models.IntegerField()
