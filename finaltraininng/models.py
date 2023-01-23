from django.db import models
from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class User(models.Model):
    userid = models.PositiveBigIntegerField(unique=True)
    balance = models.DecimalField(
        default=0,
        max_digits=100,
        decimal_places=2
    )
    def __str__(self):
        return str(self.userid)
class Training(models.Model):
    Name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        unique=True
    )
    Info = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    def __str__(self):
        return str(self.Name)

class Trainer(models.Model):
    Name = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )
    Surname = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )
    Info = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    def __str__(self):
        return str(self.Name)
class Prize(models.Model):
    Name = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )
    Prize = models.DecimalField(
        decimal_places=2,
        max_digits=5000,
        null=False
    )
    Prize2 = models.DecimalField(
        decimal_places=2,
        max_digits=15000,
        null=False
    )
    def __str__(self):
        return str(self.Name)
class Abon(models.Model):
    Name = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )
    trainin = models.ForeignKey(Training, on_delete=models.CASCADE, null=True)
    trainerin = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    prizein = models.ForeignKey(Prize, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.Name)
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prodid = models.ForeignKey(Abon, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.userid)

class Wallet(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    balance = models.DecimalField(
        default=0,
        max_digits=100,
        decimal_places=2
    )
    def __str__(self):
        return str(self.userid)