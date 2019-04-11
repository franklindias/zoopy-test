import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://api.zoop.ws/v1'

TOKEN = None
MARKETPLACE_ID = None


def validate_response(zoopy_response):
    if zoopy_response.status_code == 200:
        return zoopy_response.json()
    else:
        return error(zoopy_response.json())

def get_marketplace_id():
    return MARKETPLACE_ID

def authentication_key(api_key=None, marketplace_id=None):
    global TOKEN    
    global MARKETPLACE_ID    
    TOKEN = HTTPBasicAuth(api_key, '')
    MARKETPLACE_ID = marketplace_id


def delete(end_point, data = {}):
    url = f'{BASE_URL}{end_point}'
    zoopy_response = requests.delete(url, data=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def get(end_point, data = {}):
    url = f'{BASE_URL}{end_point}'
    zoopy_response = requests.get(url, data=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def post(end_point, data={}):
    url = f'{BASE_URL}{end_point}'
    zoopy_response = requests.post(url, data=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def put(end_point, data = {}):
    url = f'{BASE_URL}{end_point}'
    zoopy_response = requests.put(url, data=data, headers=headers(), auth=TOKEN)
    return validate_response(zoopy_response)


def error(data):
    raise Exception(data['errors'])


def headers():
    _headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    return _headers