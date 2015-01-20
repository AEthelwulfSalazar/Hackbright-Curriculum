class Square(object):
    def get_price(self):
        return super(Square, self).get_price() * 2


class Round(object):
    pass

class Melon(object):
    def get_price(self):
        return 5.00


class Squash(object):
    def get_price(self):
        return 2.50


