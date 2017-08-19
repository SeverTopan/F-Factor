from rest_framework import serializers
from .models import WbvEntry


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WbvEntry
        fields = ('team_name', 'team_symbol', 'score')
