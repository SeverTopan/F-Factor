from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from httplib2 import Http
from django.http import HttpResponse
from wbv.models import WbvEntry
from bm.models import BmEntry
from oc.models import OcEntry
from thp.models import ThpEntry
from dc.models import DcEntry
from pprint import pprint
import os
import json

# Max value stored within a PositiveIntegerField.
MAX_INT = 2147483647 

def parseInt(string):
    """
        Sanitize the string into a value that can be stored within a PositiveIntegerField.
    """

    try: 
        val = int(string)

        if val > MAX_INT or val < 0:
            return None

        return val
    except ValueError:
        return None

def update(_):
    """
        Pulls an updated copy of the data from the data source of the cache.
        In this case the data source is google sheets.
    """

    # Authentication scopes.
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    # Obtain service key.
    if os.environ.get('GOOGLE_SERVICE_KEY') is not None:
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(os.environ['GOOGLE_SERVICE_KEY']), scopes)
    else:
        credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scopes)

    # Authorize.
    http_auth = credentials.authorize(Http())

    # The spreadsheet to request.
    spreadsheet_id = '1phD9UoMwhutRabSvekdRgDUFzD9zBKWcI-7p_8_Tv0s'

    # The ranges to retrieve from the spreadsheet.
    ranges = [
        "'Water Balloon Volleyball'!A2:C19",
        "'Bring Me'!A2:C19",
        "'Obstacle Course'!A2:D19",
        "'Treasure Hunt Puzzle'!A2:D19",
        "'Design Challenge'!A2:H19",
    ]

    # Build and execute the sheets API request.
    sheets = discovery.build('sheets', 'v4', http=http_auth)
    request = sheets.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=ranges)
    response = request.execute()

    # wbv
    for entry in response['valueRanges'][0]['values']:
        WbvEntry.objects.filter(team__name=entry[1]).update(score=parseInt(entry[0]))

    # bm
    for entry in response['valueRanges'][1]['values']:
        BmEntry.objects.filter(team__name=entry[1]).update(score=parseInt(entry[0]))

    # oc
    for entry in response['valueRanges'][2]['values']:
        OcEntry.objects.filter(team__name=entry[2]).update(score=parseInt(entry[0]), time=parseInt(entry[1]))

    # thp
    for entry in response['valueRanges'][3]['values']:
        ThpEntry.objects.filter(team__name=entry[2]).update(score=parseInt(entry[0]), time=parseInt(entry[1]))

    # dc
    for entry in response['valueRanges'][4]['values']:
        DcEntry.objects.filter(team__name=entry[6]).update(
            score=parseInt(entry[0]),
            baja_score=parseInt(entry[1]), 
            baja_time=parseInt(entry[2]),
            toike_cannon_score=parseInt(entry[3]),
            wise_score=parseInt(entry[4]),
            hpv_score=parseInt(entry[5]),
        )

    # 200 response.
    return HttpResponse()

