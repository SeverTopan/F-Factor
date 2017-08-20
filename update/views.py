from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from httplib2 import Http
from django.http import HttpResponse
from wbv.models import WbvEntry
from pprint import pprint

scopes = ['https://www.googleapis.com/auth/spreadsheets']

credentials = ServiceAccountCredentials.from_json_keyfile_name('F!Factor-9533e3a8aaf0.json', scopes)

http_auth = credentials.authorize(Http())

# The spreadsheet to request.
spreadsheet_id = '1phD9UoMwhutRabSvekdRgDUFzD9zBKWcI-7p_8_Tv0s'

# The ranges to retrieve from the spreadsheet.
ranges = ["'Water Balloon Volleyball'!A2:C5"]

sheets = discovery.build('sheets', 'v4', http=http_auth)

request = sheets.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=ranges)


def update(_):
    
    response = request.execute()
    pprint(response)

    # wbv
    for entry in response['valueRanges'][0]['values']:
        WbvEntry.objects.filter(team_name=entry[1]).update(score=entry[0])

    return HttpResponse()

