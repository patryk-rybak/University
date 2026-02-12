# Creator, Information Expert, high cohesion
class Product:
    def __init__(self, name, category, manufacturer):
        self.name = name
        self.category = category
        self.manufacturer = manufacturer
        self.offers = []

    def create_offer(self, price, wholesaler):
        offer = Offer(self, price, wholesaler)
        self.offers.append(offer)
        return offer


class Offer:
    def __init__(self, product, price, wholesaler):
        self.product = product
        self.price = price
        self.wholesaler = wholesaler


class OrderPosition:
    def __init__(self, offer, quantity):
        self.offer = offer
        self.quantity = quantity

    def total_price(self):
        return self.offer.price * self.quantity


class Order:
    def __init__(self):
        self.positions = []

    def _create_position(self, offer, quantity):
        position = OrderPosition(offer, quantity)
        return position

    def add_offer_to_order(self, offer, quantity):
        position = self._create_position(offer, quantity)
        self.positions.append(position)

    def total_price(self):
        return sum([position.total_price() for position in self.positions])
