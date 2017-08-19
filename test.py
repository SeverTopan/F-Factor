from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from httplib2 import Http
from pprint import pprint

scopes = ['https://www.googleapis.com/auth/spreadsheets']

credentials = ServiceAccountCredentials.from_json_keyfile_name('F!Factor-9533e3a8aaf0.json', scopes)

http_auth = credentials.authorize(Http())

# The spreadsheet to request.
spreadsheet_id = '1phD9UoMwhutRabSvekdRgDUFzD9zBKWcI-7p_8_Tv0s'

# The ranges to retrieve from the spreadsheet.
ranges = ['\'Water Balloon Volleyball\'!A2:C5']

# True if grid data should be returned.
# This parameter is ignored if a field mask was set in the request.
include_grid_data = False

sheets = discovery.build('sheets', 'v4', http=http_auth)

request = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=include_grid_data)
response = request.execute()

pprint(response)