class SplitRole(object):

    def __init__(self, **kwargs):
        self.recipient = kwargs.get('recipient', None)
        self.liable = kwargs.get('liable', None)
        self.charge_processing_fee = kwargs.get('charge_processing_fee', None)
        self.percentage = kwargs.get('percentage', None)
        self.amount = kwargs.get('amount', None)