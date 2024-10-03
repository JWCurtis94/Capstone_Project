from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    track = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%Y-%m-%d')}"


class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()
    fastest_lap = models.BooleanField(default=False)

    class Meta:
        unique_together = ('race', 'driver')

    def __str__(self):
        return f"{self.race.name} - {self.driver.username} - P{self.position}"


class Verdict(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class IncidentTicket(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    race_name = models.CharField(max_length=255)
    incident_description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.race_name}"