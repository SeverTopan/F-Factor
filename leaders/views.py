from rest_framework.views import APIView
from rest_framework.response import Response
from wbv.models import WbvEntry
from wbv.serializers import WbvEntrySerializer
from bm.models import BmEntry
from bm.serializers import BmEntrySerializer
from oc.models import OcEntry
from oc.serializers import OcEntrySerializer
from thp.models import ThpEntry
from thp.serializers import ThpEntrySerializer
from dc.models import DcEntry
from dc.serializers import DcEntrySerializer
from django.db.models import Max, Min
from django.core.cache import cache

def _get_wbv():
    cached_val = cache.get('wbv')
    if cached_val is not None:
        return cached_val

    max_score = WbvEntry.objects.all().aggregate(score=Max('score'))['score']
    wbv = WbvEntry.objects.filter(score=max_score)
    wbv_data = WbvEntrySerializer(wbv, many=True).data[0]

    if wbv.count() > 1:
        wbv_data['team']['name'] = 'Tie!'
        wbv_data['team']['symbol'] = 'Multiple Teams'

    cache.set('wbv', wbv_data, 15)

    return wbv_data

def _get_bm():
    cached_val = cache.get('bm')
    if cached_val is not None:
        return cached_val

    max_score = BmEntry.objects.all().aggregate(score=Max('score'))['score']
    bm = BmEntry.objects.filter(score=max_score)
    bm_data = BmEntrySerializer(bm, many=True).data[0]

    if bm.count() > 1:
        bm_data['team']['name'] = 'Tie!'
        bm_data['team']['symbol'] = 'Multiple Teams'

    cache.set('bm', bm_data, 15)

    return bm_data

def _get_oc():
    cached_val = cache.get('oc')
    if cached_val is not None:
        return cached_val

    max_time = OcEntry.objects.all().aggregate(time=Min('time'))['time']
    oc = OcEntry.objects.filter(time=max_time)
    oc_data = OcEntrySerializer(oc, many=True).data[0]

    if oc.count() > 1:
        oc_data['team']['name'] = 'Tie!'
        oc_data['team']['symbol'] = 'Multiple Teams'

    cache.set('oc', oc_data, 15)

    return oc_data

def _get_thp():
    cached_val = cache.get('thp')
    if cached_val is not None:
        return cached_val

    max_time = ThpEntry.objects.all().aggregate(time=Min('time'))['time']
    thp = ThpEntry.objects.filter(time=max_time)
    thp_data = ThpEntrySerializer(thp, many=True).data[0]

    if thp.count() > 1:
        thp_data['team']['name'] = 'Tie!'
        thp_data['team']['symbol'] = 'Multiple Teams'

    cache.set('thp', thp_data, 15)

    return thp_data

def _get_dc():
    cached_val = cache.get('dc')
    if cached_val is not None:
        return cached_val

    dc_objects = DcEntry.objects.all()
    dc_data = {
        'baja': _get_dc_baja(dc_objects),
        'tc': _get_dc_tc(dc_objects),
        'wise': _get_dc_wise(dc_objects),
        'hpv': _get_dc_hpv(dc_objects),
    }

    cache.set('dc', dc_data, 15)

    return dc_data

def _get_dc_baja(objects):
    max_time = objects.aggregate(baja_time=Min('baja_time'))['baja_time']
    dc = DcEntry.objects.filter(baja_time=max_time)
    dc_data = DcEntrySerializer(dc, many=True).data[0]

    if dc.count() > 1:
        dc_data['team']['name'] = 'Tie!'
        dc_data['team']['symbol'] = 'Multiple Teams'

    return dc_data

def _get_dc_tc(objects):
    max_score = objects.aggregate(toike_cannon_score=Max('toike_cannon_score'))['toike_cannon_score']
    dc = DcEntry.objects.filter(toike_cannon_score=max_score)
    dc_data = DcEntrySerializer(dc, many=True).data[0]

    if dc.count() > 1:
        dc_data['team']['name'] = 'Tie!'
        dc_data['team']['symbol'] = 'Multiple Teams'

    return dc_data

def _get_dc_wise(objects):
    max_score = objects.aggregate(wise_score=Max('wise_score'))['wise_score']
    dc = DcEntry.objects.filter(wise_score=max_score)
    dc_data = DcEntrySerializer(dc, many=True).data[0]

    if dc.count() > 1:
        dc_data['team']['name'] = 'Tie!'
        dc_data['team']['symbol'] = 'Multiple Teams'

    return dc_data

def _get_dc_hpv(objects):
    max_score = objects.aggregate(hpv_score=Max('hpv_score'))['hpv_score']
    dc = DcEntry.objects.filter(hpv_score=max_score)
    dc_data = DcEntrySerializer(dc, many=True).data[0]

    if dc.count() > 1:
        dc_data['team']['name'] = 'Tie!'
        dc_data['team']['symbol'] = 'Multiple Teams'

    return dc_data

class LeaderView(APIView):

    def get(self, request, format=None):
        wbv_data = _get_wbv()
        bm_data = _get_bm()
        oc_data = _get_oc()
        thp_data = _get_thp()
        dc_data = _get_dc()

        return Response({ 
            'wbv': wbv_data,
            'bm': bm_data,
            'oc': oc_data,
            'thp': thp_data,
            'dc': dc_data,
            })

class WbvLeaderView(APIView):

    def get(self, request, format=None):
        wbv_data = _get_wbv()

        return Response({ 
            'wbv': _get_wbv(),
            })

class BmLeaderView(APIView):

    def get(self, request, format=None):
        bm_data = _get_bm()

        return Response({ 
            'bm': _get_bm(),
            })

class OcLeaderView(APIView):

    def get(self, request, format=None):
        oc_data = _get_oc()

        return Response({ 
            'oc': _get_oc(),
            })

class ThpLeaderView(APIView):

    def get(self, request, format=None):
        thp_data = _get_thp()

        return Response({ 
            'thp': _get_thp(),
            })

class DcLeaderView(APIView):

    def get(self, request, format=None):
        dc_data = _get_dc()

        return Response({ 
            'dc': _get_dc(),
            })