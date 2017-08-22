from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ThpEntry
from .serializers import ThpEntrySerializer

class ThpEntryList(APIView):

    def get(self, request, format=None):
        thp = ThpEntry.objects.all().order_by('team__name')
        serializer = ThpEntrySerializer(thp, many=True)
        return Response(serializer.data)
