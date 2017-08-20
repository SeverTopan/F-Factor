from rest_framework.views import APIView
from rest_framework.response import Response
from wbv.models import WbvEntry
from wbv.serializers import WbvEntrySerializer
from django.db.models import Max

class LeaderView(APIView):

    def get(self, request, format=None):

        max_score = WbvEntry.objects.all().aggregate(score=Max('score'))['score']
        wbv = WbvEntry.objects.filter(score=max_score)
        wbv_data = WbvEntrySerializer(wbv, many=True).data[0]

        if wbv.count() > 1:
            wbv_data['team']['name'] = 'Tie!'
            wbv_data['team']['symbol'] = '='


        return Response({ 'wbv': wbv_data })