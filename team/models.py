from django.db import models

class Team(models.Model):
    name = models.TextField()
    symbol = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
