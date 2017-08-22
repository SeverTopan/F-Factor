from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WbvEntry
from .serializers import WbvEntrySerializer

class WbvEntryList(APIView):

    def get(self, request, format=None):
        wbv = WbvEntry.objects.all().order_by('team__order')
        serializer = WbvEntrySerializer(wbv, many=True)
        return Response(serializer.data)
