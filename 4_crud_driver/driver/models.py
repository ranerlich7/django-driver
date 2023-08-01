from email.mime import audio
from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.username} - {self.team}"

    def races(self):
        return list(self.race_set.all())

    # Meta is definitions for this class
    # verbose name is the name that will be shown in Admin instead of "User"

    class Meta:
        verbose_name = "Driver"


class Race(models.Model):
    name = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(null=False)
    driver = models.ManyToManyField(Driver)

    def __str__(self):
        return self.name
