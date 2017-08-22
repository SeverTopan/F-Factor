from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OcEntry
from .serializers import OcEntrySerializer

class OcEntryList(APIView):

    def get(self, request, format=None):
        thp = OcEntry.objects.all().order_by('team__order')
        serializer = OcEntrySerializer(thp, many=True)
        return Response(serializer.data)
