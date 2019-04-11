from models import Seller

class SellerIndividual(Seller):

    def __init__(self, **kwargs):
        self.type = 'individual'        
        self.statement_descriptor = None
        self.delinquent = None
        super(SellerIndividual, self).__init__(**kwargs)