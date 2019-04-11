from models import Marketplace, SellerBusiness
from utils import authentication_key

authentication_key(api_key='zpk_test_ISLmKnlXiHGSsgjanvN6gbOJ', marketplace_id="033ef887928e4fbb915276fa709993ed")

data = {
    'id': '7355b0f00ade4e5d88648c5f8f02681b', 
    'status': 'enabled', 
    'resource': 'seller', 
    'type': 'business', 
    'description': 'Marketplace de Testes Cubo Hub', 
    'account_balance': '0.00', 
    'current_balance': '0.00', 
    'business_name': 'One Empreendimentos Servicos Combinados Eireli Me', 
    'business_phone': '84988752710', 
    'business_email': 'guilhermehenrique@seawaycenter.com', 
    'business_website': '', 
    'business_description': 'Cubo Hub', 
    'business_opening_date': '2017-11-30', 
    'business_facebook': '', 
    'business_twitter': None, 
    'ein': '29253808000162', 
    'statement_descriptor': 
    'cubohub', 
    'mcc': '18', 
    'business_adress': {
        'line1': 'Av Engenheiro Roberto Freire', 
        'line2': '1962', 
        'line3': 'loja 26', 
        'neighborhood': 'Capim Macio', 
        'city': 'Natal', 
        'state': 'RN', 
        'postal_code': '59082095', 
        'country_code': 'BR'
    }, 
    'owner': {
        'first_name': 'Guilherme', 
        'last_name': 'Oliveira', 
        'email': 'guilhermehenrique@seawaycenter.com', 
        'phone_number': None, 
        'taxpayer_id': None, 
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
    'default_credit': None, 
    'merchant_code': '012000000000001', 
    'terminal_code': 'GT0000CA', 
    'uri': '/v1/marketplaces/55113f2bdef54dfc8c89e71c35d41c4c', 
    'marketplace_id': '033ef887928e4fbb915276fa709993ed', 
    'metadata': {}, 
    'created_at': '2019-04-10T13:42:12+00:00', 
    'updated_at': '2019-04-10T13:42:39+00:00'}

seller = SellerBusiness(**data)

seller = seller.get_list()

print(seller)