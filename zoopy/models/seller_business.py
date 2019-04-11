from models import Seller

class SellerBusiness(Seller):

    def __init__(self, **kwargs):
        self.type = 'business'        
        self.owner = kwargs.get('owner', None)        
        self.business_name = kwargs.get('business_name', None)
        self.business_phone = kwargs.get('business_phone', None)
        self.busines_website = kwargs.get('busines_website', None)
        self.business_description = kwargs.get('business_description', None)
        self.business_facebook = kwargs.get('business_facebook', None)
        self.business_twitter = kwargs.get('business_twitter', None)
        self.statement_descriptor = kwargs.get('statement_descriptor', None)
        self.business_address = kwargs.get('business_address', None)
        self.business_opening_date = kwargs.get('business_opening_date', None)
        self.owner_address = kwargs.get('owner_address', None)
        self.delinquent = kwargs.get('delinquent', None)
        super(SellerBusiness, self).__init__(**kwargs)