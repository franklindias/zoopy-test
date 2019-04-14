from zoopy.utils import get, put, post, delete
from zoopy.models import marketplace 

BASE_MODEL_URL = '/transactions'

def full_url(self):
    return BASE_MODEL_URL

def list():
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url)

def details(transaction_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{id}'
    return get(url)

def create(params):
    url = f'{marketplace.get_full_url()}{full_url}'
    return post(end_point=url, data=params)

def update(self):
    url = f'{marketplace.get_full_url()}{full_url}/{id}'
    return put(end_point=url, data=params)