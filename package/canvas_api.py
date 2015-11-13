### Code to import CSV files into Canvas
from config import *
import requests
import json
#csvExportLocation = "G:/Inbox/"
#token = "5278~XiOGA1DzWNO1dYvtHtgbHOcIGSlYQI2HVghE3EcnoEBlnF0H3kTo3cDI10DdPm1K"
#account_id = 1
#base_api_url = 'https://ecasd.test.instructure.com/api/'


### Post csv or zip file for Sis Import. Just change the file name.
def sisIMPORT():
    path = 'v1/accounts/{account_id}/sis_imports'
    url = Canvas_base_api_url + path.format(account_id=Canvas_account_id)
    files = {'attachment': open('{csvExportLocation}courses.csv'.format(csvExportLocation = csvExportLocation), 'rb')}
    headers = {'Authorization':'Bearer {token}'.format(token=CanvasSISImportToken)}
    res = requests.post(url, files=files, headers = headers)
    return ('SIS Import Complete')
    
    
def sis_import_status():
    """
    Will give the status of the last sis Import
    """
    ### Get status of last SIS imports
    path = 'v1/accounts/{account_id}/sis_imports'
    url = Canvas_base_api_url + path.format(account_id=Canvas_account_id)
    headers = {'Authorization':'Bearer {token}'.format(token=CanvasSISImportToken)}
    r = requests.get(url, headers=headers)
    rJson = r.json()
    print(rJson['sis_imports'][0])
    return print('Thats It')