from models import Address

class Owner(object):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
            
        _addrres = kwargs.get('address')
        if _addrres and not isinstance(_addrres, Address)::
            self.address = Address(**self.address)