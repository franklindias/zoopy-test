class Paginator(object):
    def __init__(self, Sender, **kwargs):
        self.resource = kwargs.get('resource', None)
        self.uri = kwargs.get('resource', None)
        self.has_more = kwargs.get('has_more', None)
        self.limit = kwargs.get('limit', None)
        self.total_pages = kwargs.get('total_pages', None)
        self.page = kwargs.get('page', None)
        self.offset = kwargs.get('offset', None)
        self.total = kwargs.get('total', None)
        self.query_count = kwargs.get('query_count', None)
        self.items = kwargs.get('items', None)
        self.set = []
        
        for item in self.items:
            self.set.append(Sender(**item))