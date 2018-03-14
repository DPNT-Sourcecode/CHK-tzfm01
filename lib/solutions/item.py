class Item(object):
    """
    This is a item, product from the supermarket basket
    """
    def __init__(self, price, offers):
        self.price = price
        self.offers = offers
        self.quantity = 0
        self.totat_price = 0
        self.parent = []

    def 