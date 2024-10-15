from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    balance = models.DecimalField(decimal_places=2, max_digits=8)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=300)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    size = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
