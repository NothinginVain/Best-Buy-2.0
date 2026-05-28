from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for product promotions.
    """

    def __init__(self, name):
        """
        Initialize a promotion.

        Args:
            name (str): Name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply promotion to a purchase.

        Args:
            product (any): Product or price reference.
            quantity (int): Quantity purchased.

        Returns:
            float: Discounted total price.
        """
        pass


class PercentDiscount(Promotion):
    """
    Percentage-based discount promotion.
    """

    def __init__(self, name, percent):
        """
        Initialize percentage discount promotion.

        Args:
            name (str): Promotion name.
            percent (float): Discount percentage.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        """
        Apply percentage discount to total price.
        """
        total = quantity * price
        percent_off = total * (self.percent / 100)
        return total - percent_off


class SecondHalfPrice(Promotion):
    """
    Promotion where every second item is half price.
    """

    def apply_promotion(self, price, quantity):
        """
        Apply second item half-price promotion.
        """
        pairs = quantity // 2
        leftover = quantity % 2

        pair_price = pairs * (price + price / 2)
        leftover_price = leftover * price

        return pair_price + leftover_price


class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """

    def apply_promotion(self, price, quantity):
        """
        Apply "buy 2 get 1 free" promotion.
        """
        groups_of_three = quantity // 3
        leftover = quantity % 3

        paid_items = groups_of_three * 2 + leftover

        return paid_items * price