from utils import get, put, post, delete, get_marketplace_id 
from utils import Paginator, ObjectJSON
from models import Marketplace, Owner, Address


class Seller(ObjectJSON):

    BASE_MODEL_URL = '/sellers'
    INDIVIDUALS_URL = BASE_MODEL_URL + "/individuals"
    BUSINESSES_URL = BASE_MODEL_URL + "/businesses"

    def __init__(self, **kwargs):
        self.type = kwargs.get('type', None)     
        self.marketplace = Marketplace(id=kwargs.get('marketplace_id', get_marketplace_id()))
        self.id = kwargs.get('id', None)
        self.resource = kwargs.get('resource', None)
        self.status = kwargs.get('status', None)
        self.taxpayer_id = kwargs.get('taxpayer_id', None)
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

        #SELLER BUSINESS
        self.owner = Owner(**kwargs.get('owner', {}))       
        self.business_name = kwargs.get('business_name', None)
        self.business_phone = kwargs.get('business_phone', None)
        self.busines_website = kwargs.get('busines_website', None)
        self.business_description = kwargs.get('business_description', None)
        self.business_facebook = kwargs.get('business_facebook', None)
        self.business_twitter = kwargs.get('business_twitter', None)
        self.statement_descriptor = kwargs.get('statement_descriptor', None)
        self.business_opening_date = kwargs.get('business_opening_date', None)
        self.delinquent = kwargs.get('delinquent', None)

        owner = kwargs.get('owner', None)
        self.owner = Owner(**owner) if owner else None

        business_address = kwargs.get('business_address', None)
        self.business_address = Address(**business_address) if business_address else None

    @property
    def full_url(self):
        print(self.type)
        if self.type == 'business':
            return self.BUSINESSES_URL

        return self.INDIVIDUALS_URL

    @classmethod
    def list(self):
        marketplace = Marketplace(id=get_marketplace_id())
        url = f'{marketplace.full_url}{self.BASE_MODEL_URL}'
        return Paginator(Sender=Seller, **get(url))

    def details(self):
        url = f'{self.marketplace.full_url}{self.BASE_MODEL_URL}/{self.id}'
        self.__init__(**get(url))
        return self
    
    def create(self):
        url = f'{self.marketplace.full_url}{self.full_url}'
        self.__init__(**post(end_point=url, data=self.toJSON()))
        return self
    
    def update(self):
        url = f'{self.marketplace.full_url}{self.full_url}/{self.id}'
        self.__init__(**put(end_point=url, data=self.toJSON()))
        return self

    def delete(self):
        url = f'{self.marketplace.full_url}{self.BASE_MODEL_URL}/{self.id}'
        return delete(url)