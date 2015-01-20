# class Square(object):
#     def get_price(self):
#         return super(Square, self).get_price() * 2


# class Round(object):
#     pass

class Melon(object):
    base_price = price = 5.00
    def get_price(self, qty):
        price = self.base_price
        if self.is_imported == True:
            price *= 1.5
        if self.shape == "square":
            price *= 2
        return price * qty


class Watermelon(Melon):
    color = 'green'
    is_imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
        

class Cantaloupe(Melon):
    color = 'tan'
    is_imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        price = super(Cantaloupe, self).get_price(qty)
        if qty >= 5:
            return price / 2
        return price


class Casaba(Melon):
    base_price = 6.00
    color = 'green'
    is_imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']


class Sharlyn(Melon):
    color = 'tan'
    is_imported = True
    shape = 'natural'
    seasons = ['Summer']


class SantaClaus(Melon):
    color = 'green'
    is_imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']


class Christmas(Melon):
    color = 'green'
    is_imported = False
    shape = 'natural'
    seasons = ['Winter']


class HornedMelon(Melon):
    color = 'yellow'
    is_imported = True
    shape = 'natural'
    seasons = ['Summer']


class Xigua(Melon):
    color = 'black'
    is_imported = True
    shape = 'square'
    seasons = ['Summer']

class Ogen(Melon):
    base_price = 6.00
    color = 'tan'
    is_imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

# class Squash(object):
#     def get_price(self):
#         return 2.50


