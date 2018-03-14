class Item(object):
    """
    This is a item, product from the supermarket basket
    """
    def __init__(self, price, offers):
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