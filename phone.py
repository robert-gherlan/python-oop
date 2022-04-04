from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self project
        self.broken_phones = broken_phones
