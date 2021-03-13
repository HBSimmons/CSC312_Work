# Flower class for flower name, petal count, and price

class Flower:
    def __init__(self, name, ptlct, price): # creating a new flower instance
        self._name = name
        self._ptlct = ptlct
        self._price = price

    def get_name(self):
        return self._name # returns name of flower

    def get_ptlct(self):
        return self._ptlct # returns petal count

    def get_price(self):
        return self._price # returns price

    def set_name(self, name):
        self._name = name  # sets name

    def set_ptlct(self, ptlct):
        self._ptlct = ptlct  # sets petal count

    def set_price(self, price):
        self._price = price # sets price


