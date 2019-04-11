class Marketplace(object):

    MODEL_BASE_URL = '/marketplaces'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)

    def get_url(self):
        return f'{self.MODEL_BASE_URL}/{self.id}'

    def get_details(self):        
        return self.get(self.get_url)