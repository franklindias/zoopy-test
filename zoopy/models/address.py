class Address(object):

    def __init__(self, **kwargs):
        self.line1 = kwargs.get('line1', None)
        self.line2 = kwargs.get('line2', None)
        self.line3 = kwargs.get('line3', None)
        self.neighborhood = kwargs.get('neighborhood', None)
        self.city = kwargs.get('city', None)
        self.state = kwargs.get('state', None)
        self.postal_code = kwargs.get('postal_code', None)
        self.country_code = kwargs.get('country_code', None)