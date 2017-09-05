from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ThpEntry
from .serializers import ThpEntrySerializer

class ThpEntryList(APIView):

    def get(self, request, format=None):
        """
            Obtain all wbv entries as a list.
        """
        
        thp = ThpEntry.objects.all().order_by('team__order')
        serializer = ThpEntrySerializer(thp, many=True)
        return Response(serializer.data)
