from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BmEntry
from .serializers import BmEntrySerializer

class BmEntryList(APIView):

    def get(self, request, format=None):
        wbv = BmEntry.objects.all().order_by('team__order')
        serializer = BmEntrySerializer(wbv, many=True)
        return Response(serializer.data)
