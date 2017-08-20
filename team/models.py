from django.db import models

class Team(models.Model):
    name = models.TextField()
    symbol = models.TextField()

    def __str__(self):
        return self.name
    
