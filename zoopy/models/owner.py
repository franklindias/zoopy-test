class Owner(object):
    
    def __init__(self, **kwargs):
        self.taxpayer_id = kwargs.get('taxpayer_id', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.email = kwargs.get('email', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.birthdate = kwargs.get('birthdate', None)