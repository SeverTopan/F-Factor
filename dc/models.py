from django.db import models
from team.models import Team

class DcEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    score = models.PositiveIntegerField()
    baja_time = models.PositiveIntegerField()
    baja_score = models.PositiveIntegerField()
    toike_cannon_score = models.PositiveIntegerField()
    wise_score = models.PositiveIntegerField()
    hpv_score = models.PositiveIntegerField()


    def __str__(self):
        return self.team.name
    
