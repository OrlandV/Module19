from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=150)
    balance = models.DecimalField(decimal_places=2, max_digits=8, default=0.00)
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


class Review(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    game = models.ForeignKey(Game, models.DO_NOTHING)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING)

    def __str__(self):
        return self.title
