from email.mime import audio
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100, null=False)
    # default age is 0 to accomodate superuser for example
    age = models.IntegerField(default=0)
    # team can be null
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    # you can also use
    #        REQUIRED_FIELDS = ["date_of_birth", "height"]

    def __str__(self):
        return f"{self.name} - {self.team}"


class Race(models.Model):
    name = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(null=False)
    driver = models.ManyToManyField(Driver)

    def __str__(self):
        return self.name
