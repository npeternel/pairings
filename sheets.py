from __future__ import print_function
import httplib2
import os
#from main import rankNum

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getData(spreadsheet_id):
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    #rank = rankNum()
    rank = 3 # shouldn't be hardcoded
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    #spreadsheetId = '1K7uC_Jezx4nNeiKP90HaPgq2v24TTaT37Z5QHdz6wAI'
    spreadsheetId = spreadsheet_id
    rangeEnd = chr((rank+2) + ord('A'))
    rangeName = 'Sheet1!B2:' + rangeEnd
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    a_pref = {}
    b_pref = {}

    if not values:
        print('No data found.')
    else:
        for row in values:
            if row[0] == "A":
                a_pref[row[1]] = row[2:]
            elif row[0] == "B":
                b_pref[row[1]] = row[2:]
            else:
                print("AHHH SOMETHING'S WRONG MAYBE DO AN ERROR THING")
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s: %s, [%s, %s, %s]' % (row[0], row[1], row[2], row[3], row[4]))
    print(b_pref)
    return a_pref, b_pref

'''def writeResults():
    # write practice start
    writeToId = '1w1FZSpHGMVa4YQyUvPWFabNXJrP-fsybQEi83q1zjpw'
    values = [
        [
            1, 2, 3
        # Cell values ...
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    value_input_option = "RAW"
    result = service.spreadsheets().values().update(
    spreadsheetId=writeToId, range="Result",
    valueInputOption=value_input_option, body=body).execute()
    "range": "Sheet1!A1:D5",
        "majorDimension": "ROWS",
        "values": [
            ["Item", "Cost", "Stocked", "Ship Date"],
            ["Wheel", "$20.50", "4", "3/1/2016"],
            ["Door", "$15", "2", "3/15/2016"],
            ["Engine", "$100", "1", "30/20/2016"],
            ["Totals", "=SUM(B2:B4)", "=SUM(C2:C4)", "=MAX(D2:D4)"]
        ],'''
    # write practice end


