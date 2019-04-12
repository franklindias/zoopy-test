from models import Marketplace, Seller, Owner, Address
from utils import authentication_key

authentication_key(api_key='zpk_test_ISLmKnlXiHGSsgjanvN6gbOJ', marketplace_id="033ef887928e4fbb915276fa709993ed")

data = {
    'status': 'enabled', 
    'resource': 'seller', 
    'type': 'business', 
    'description': 'Novo Seller', 
    'account_balance': '0.00', 
    'current_balance': '0.00', 
    'business_name': 'Business novo', 
    'business_phone': '84988752710', 
    'business_email': 'franklindias@seawaycenter.com', 
    'business_website': '', 
    'business_description': 'Cubo Hub', 
    'business_opening_date': '2017-11-30', 
    'business_facebook': '', 
    'business_twitter': None, 
    'ein': '61767956000108', 
    'statement_descriptor': 
    'cubohub', 
    'mcc': '18', 
    'business_adress': {
        'line1': 'adasd', 
        'line2': '1962', 
        'line3': 'loja 26', 
        'neighborhood': 'Capim Macio', 
        'city': 'Natal', 
        'state': 'RN', 
        'postal_code': '59082095', 
        'country_code': 'BR'
    }, 
    'owner': {
        'first_name': 'dasd', 
        'last_name': 'Olivadasdeira', 
        'email': 'dasdasdc@seawaycenter.com', 
        'phone_number': None, 
        'taxpayer_id': "09024942446", 
        'birthdate': None, 
        'address': {
            'line1': "rua linha 1", 
            'line2': None, 
            'line3': None, 
            'neighborhood': None, 
            'city': None, 
            'state': None, 
            'postal_code': None, 
            'country_code': None
        }
    }, 
    'show_profile_online': False, 
    'is_mobile': False, 
    'decline_on_fail_security_code': True, 
    'decline_on_fail_zipcode': False, 
    'delinquent': False, 
    'payment_methods': None, 
    'default_debit': None, 
    'default_credit': None,}

address = Address(line1="Nova rua de teste")
seller = Seller(id="7355b0f00ade4e5d88648c5f8f02681b", address=address, type="business")

seller = seller.update()

print(seller.address.line1)

