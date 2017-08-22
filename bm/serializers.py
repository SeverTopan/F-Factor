from rest_framework import serializers
from .models import BmEntry
from team.models import Team
from team.serializers import TeamSerializer


class BmEntrySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = BmEntry
        fields = ('team', 'score')
