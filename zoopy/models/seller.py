from utils import get, put, post, delete, get_marketplace_id 
from utils import Paginator, ObjectJSON
from models import Marketplace, Owner, Address


class Seller(ObjectJSON):

    BASE_MODEL_URL = '/sellers'
    INDIVIDUALS_URL = BASE_MODEL_URL + "/individuals"
    BUSINESSES_URL = BASE_MODEL_URL + "/businesses"

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
   
        self.marketplace = Marketplace(id=kwargs.get('marketplace_id', get_marketplace_id()))
       
        _owner =  kwargs.get('owner')
        if _owner and not isinstance(_owner, Owner):
            self.owner = Owner(**self.owner) 

        _addrres = kwargs.get('business_address')
        if _addrres and not isinstance(_addrres, Address):
            self.business_address = Address(**self.business_address)


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