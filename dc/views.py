from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DcEntry
from .serializers import DcEntrySerializer

class DcEntryList(APIView):

    def get(self, request, format=None):
        thp = DcEntry.objects.all().order_by('team__order')
        serializer = DcEntrySerializer(thp, many=True)
        return Response(serializer.data)
