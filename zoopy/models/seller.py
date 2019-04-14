from zoopy.utils import get, put, post, delete, get_marketplace_id
from zoopy.models import marketplace


BASE_MODEL_URL = '/sellers'
INDIVIDUALS_URL = f"{BASE_MODEL_URL}/individuals"
BUSINESSES_URL = f"{BASE_MODEL_URL}/businesses"
   

def get_full_url(seller_type):
    if seller_type == 'business':
        return BUSINESSES_URL
    return INDIVIDUALS_URL

def list(seller_type):
    marketplace_id = get_marketplace_id()
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}'
    return get(url)

def details(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}'
    return get(url)

def create(params):
    url = f'{marketplace.get_full_url()}{get_full_url()}'
    return post(end_point=url, data=params)

def update(seller_id, params):
    url = f'{marketplace.get_full_url()}{get_full_url()}/{seller_id}'
    return put(end_point=url, data=params)

def delete(seller_id):
    url = f'{marketplace.get_full_url()}{BASE_MODEL_URL}/{seller_id}'
    return delete(url)