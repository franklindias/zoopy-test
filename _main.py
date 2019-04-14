# from zoopy.models import Marketplace, Seller, Owner, Address, Buyer, Transaction
from zoopy.utils import authentication_key
import zoopy

authentication_key(
        api_key='zpk_test_ISLmKnlXiHGSsgjanvN6gbOJ', 
        marketplace_id="033ef887928e4fbb915276fa709993ed"
    )

results = zoopy.transaction.list()

print(results)