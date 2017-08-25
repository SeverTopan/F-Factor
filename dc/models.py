from django.db import models
from team.models import Team

class DcEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    score = models.PositiveIntegerField(null=True)
    baja_time = models.PositiveIntegerField(null=True)
    baja_score = models.PositiveIntegerField(null=True)
    toike_cannon_score = models.PositiveIntegerField(null=True)
    wise_score = models.PositiveIntegerField(null=True)
    hpv_score = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.team.name
    
