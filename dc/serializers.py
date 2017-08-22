from rest_framework import serializers
from .models import DcEntry
from team.models import Team
from team.serializers import TeamSerializer


class DcEntrySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = DcEntry
        fields = ('team', 'score', 'team','score','baja_time','baja_score','toike_cannon_score','wise_score','hpv_score')
