from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class race(models.Model):
    name = models.Charfield(max_length=100)
    date = models.DateTimeField()
    track = models.Charfield(max_length)

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%Y-%m-%d')}"

class RaceResult(models.Modeel):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()
    fastest_lap = models.BooleanField(default=False)

    class Meta:
        unique_together = ('race', 'driver')

    def __str__(self):
        return f"{self.race.name} - {self.driver.username} - P{self.position}"