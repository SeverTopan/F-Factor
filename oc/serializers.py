from rest_framework import serializers
from .models import OcEntry
from team.models import Team
from team.serializers import TeamSerializer


class OcEntrySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = OcEntry
        fields = ('team', 'score', 'time')
