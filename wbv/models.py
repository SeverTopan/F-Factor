from django.db import models

class WbvEntry(models.Model):
    team_name = models.TextField()
    team_symbol = models.TextField()
    score = models.PositiveIntegerField()


    def __str__(self):
        return self.team_name
    
