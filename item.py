import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount. This is a class attribute.
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self project
        self.__quantity = quantity
        self.__name = name  # Means private field and can't be accessed outside the class
        self.__price = price

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):  # This represents a getter
        return self.__name

    @name.setter  # This represents a setter
    def name(self, name):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def quantity(self) -> float:
        return self.__quantity

    @property
    def read_only_name(self):
        return "AAA"

    def calculate_total_price(self) -> float:
        return self.__quantity * self.__price

    def apply_discount(self) -> None:
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value: int) -> None:
        self.__price = self.__price * + self.__price * increment_value

    def __connect(self, smtp_server=None):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, CompanyName.
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

    @classmethod
    def instantiate_from_csv(cls) -> None:  # Class method
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))

    @staticmethod
    def is_integer(num) -> bool:
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.__quantity})"
