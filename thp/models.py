from django.db import models
from team.models import Team

class ThpEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    score = models.PositiveIntegerField(null=True)
    time = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.team.name
    
