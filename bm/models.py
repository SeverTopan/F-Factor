from django.db import models
from team.models import Team

class BmEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    score = models.PositiveIntegerField()


    def __str__(self):
        return self.team.name
    
