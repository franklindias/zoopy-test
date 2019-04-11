from utils import get

from models import Seller
from models import Owner, Address


class SellerBusiness(Seller):
    def __init__(self, **kwargs):
        self.type = 'business'        
        self.owner = Owner(**kwargs.get('owner', {}))       
        self.business_name = kwargs.get('business_name', None)
        self.business_phone = kwargs.get('business_phone', None)
        self.busines_website = kwargs.get('busines_website', None)
        self.business_description = kwargs.get('business_description', None)
        self.business_facebook = kwargs.get('business_facebook', None)
        self.business_twitter = kwargs.get('business_twitter', None)
        self.statement_descriptor = kwargs.get('statement_descriptor', None)
        self.business_address = Address(**kwargs.get('business_address', {}))
        self.business_opening_date = kwargs.get('business_opening_date', None)
        self.delinquent = kwargs.get('delinquent', None)
        super(SellerBusiness, self).__init__(**kwargs)

    def get_details(self):
        url = f'{self.marketplace.get_url()}{self.get_url()}'
        self.__init__(**get(url))
        return self