from item import Item


class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int = 0):
        super().__init__(name, price, quantity)
