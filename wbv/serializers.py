from rest_framework import serializers
from .models import WbvEntry
from team.models import Team
from team.serializers import TeamSerializer


class WbvEntrySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = WbvEntry
        fields = ('team', 'score')
