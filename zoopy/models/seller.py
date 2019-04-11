from utils import get

class Seller(object):

    BASE_MODEL_URL = '/sellers'

    def __init__(self, marketplace, **kwargs):
        self.marketplace = marketplace
        self.id = kwargs.get('id', None)
        self.resource = 'seller'
        self.status = kwargs.get('status', None)
        self.taxpayer_id = kwargs.get('taxpayer_id', None)
        self.type = kwargs.get('type', None)
        self.description = kwargs.get('description', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.email = kwargs.get('email', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.mcc = kwargs.get('mcc', None)
        self.birthdate = kwargs.get('birthdate', None)
        self.facebook = kwargs.get('facebook', None)
        self.twitter = kwargs.get('twitter', None)
        self.ein = kwargs.get('ein', None)
        self.address = kwargs.get('address', None)
        self.default_debit = kwargs.get('default_debit', None)
        self.default_credit = kwargs.get('default_credit', None)
        self.is_mobile = kwargs.get('is_mobile', None)
        self.show_profile_online = kwargs.get('show_profile_online', None)
        self.account_balance = kwargs.get('account_balance', None)
        self.current_balance = kwargs.get('current_balance', None)
        self.fiscal_responsability = kwargs.get('fiscal_responsability', None)
        self.metadata = kwargs.get('metadata', None)
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)

    def get_url(self):
        return f'{self.marketplace.get_url()}{self.BASE_MODEL_URL}/{self.id}'

    def get_details(self):
        return self.marketplace.get(self.get_url())

    def get_list(self):
        url = f'{self.marketplace.get_url()}{self.BASE_MODEL_URL}'
        return get(url)