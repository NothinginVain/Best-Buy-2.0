from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        total = quantity * price
        percent_off = total * (self.percent / 100)
        return total - percent_off


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity):
        pairs = quantity // 2
        leftover = quantity % 2

        pair_price = pairs * ( price + price / 2 )
        leftover_price = leftover * price

        return pair_price + leftover_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity):
        groups_of_three = quantity // 3
        leftover = quantity % 3

        paid_items = groups_of_three * 2 + leftover

        return paid_items * price


