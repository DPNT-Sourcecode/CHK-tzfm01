import re

OFFERS_RULES = {
    'itemx': '^(?P<group_quantity>[1-9]+)[A-Z] for (?P<group_price>[0-9]+)$',
    'one_for_free': '^(?P<group_quantity>[1-9]+)[A-Z] get one {} free$',
    'nX_Y_free': '^(?P<group_quantity>[1-9]+)[A-Z] get one (?P<item>[A-Z]) free$'
}


class Item(object):
    """
    This is a item, product from the supermarket basket
    """
    def __init__(self, item, price, offers):
        self.type = item
        self.price = price
        self.offers = offers
        self._quantity = 0
        self.total_price = 0
        self.parent = []

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def quantity(self):
        return self.quantity

    def update_quantity(self, n):
        self._quantity -= n
        # this is from outside; should recalculate the price when this happens
        # self.calculate_price()

    def individual_price(self):
        self.total_price += self._quantity * self.price

    def itemx(self, x, group_price):
        """
        Offers like  1 for 3£, 2 for 5£
        :param x:
        :param group_price:
        :return:
        """
        included_offers = self._quantity // x
        self._quantity = self._quantity % x
        self.total_price += included_offers * group_price

    def one_for_free(self, x):
        """
        Offers like buy 3 get one free
        :param x:
        :return:
        """
        included_offers = self._quantity // (x + 1)
        self._quantity = self._quantity % (x + 1)
        self.total_price += included_offers * x * self.price

    def nX_Y_free(self, n, y):
        """
        Offers like 3R get one Q free
        :param n:
        :param y:
        :return:
        """
        included_offers = self._quantity // n
        for item in self.parent:
            if item.type == y:
                item.update_quantity(included_offers)

    def calculate_parents(self, all_items):
        """
        Match rules like 3R get one Q free "^(?P<group_quantity>[1-9]+)[A-Z] get one (?P<item>[A-Z]) free$"
        I need this to calculate dependencies. The parents price calculation depends on current item offers.
        Therefore the parent needs to be calculated last.
        :return:
        """
        for offer in self.offers:
            result = re.match(OFFERS_RULES['nX_Y_free'], offer)
            if result:
                group_quantity = result.groupdict()['group_quantity']
                p = result.groupdict()['item']
                for item in all_items:
                    if item.type == p:
                        self.parent.append(item)

    def calculate_price(self):
        methods = {
            'itemx': self.itemx,
            'one_for_free': self.one_for_free,
            'nX_Y_free': self.nX_Y_free
        }
        for offer in self.offers:
            for rule in OFFERS_RULES:
                if rule == 'one_for_free':
                    rule = rule.format(self.type)
                result = re.match(OFFERS_RULES['rule'], offer)
                if not result:
                    continue
                methods[rule](result.groupdict()['group_quantity'], result.groupdict()['item'])