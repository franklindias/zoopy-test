class Paginator(object):
    def __init__(self, Sender, **kwargs):
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

        self.set = []
        for item in self.items:
            self.set.append(Sender(**item))