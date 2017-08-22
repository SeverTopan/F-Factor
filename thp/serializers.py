from rest_framework import serializers
from .models import ThpEntry
from team.models import Team
from team.serializers import TeamSerializer


class ThpEntrySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = ThpEntry
        fields = ('team', 'score', 'time')
