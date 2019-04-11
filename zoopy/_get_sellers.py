from models import Marketplace, Seller
from utils import authentication_key

m = Marketplace(id='033ef887928e4fbb915276fa709993ed')

authentication_key('zpk_test_ISLmKnlXiHGSsgjanvN6gbOJ')

sellers = Seller(marketplace=m)

response = sellers.get_list()
print(response)