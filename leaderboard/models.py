from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Entry(models.Model):
    name = models.TextField()
    display_score = models.PositiveIntegerField()
    real_score = models.PositiveIntegerField()

    def __unicode__(self):
        return '[{display_score}] {real_score} : {name}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')
    
    def as_dict(self):
        return {'name': self.name, 'display_score': self.display_score, 'real_score': self.real_score}