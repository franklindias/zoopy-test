class Buyer(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.resource = kwargs.get('resource', None)
        self.description = kwargs.get('description', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.taxpayer_id = kwargs.get('taxpayer_id', None)
        self.email = kwargs.get('email', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.birthdate = kwargs.get('birthdate', None)
        self.facebook = kwargs.get('facebook', None)
        self.twitter = kwargs.get('twitter', None)
        self.email_optin = kwargs.get('email_optin', None)
        self.sms_optin = kwargs.get('sms_optin', None)
        self.default_receipt_delivery_method = kwargs.get('default_receipt_delivery_method', None)
        self.address = kwargs.get('address', None)
        self.payment_methods = kwargs.get('payment_methods', None)
        self.default_debit = kwargs.get('default_debit', None)
        self.default_credit = kwargs.get('default_credit', None)
        self.metadata = kwargs.get('metadata', None)
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)