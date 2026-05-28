from promotions import Promotion
from typing import Optional, Any

class Product:

    def __init__(self, name: str, price: float, quantity: int):

        if not name or not isinstance(name, str):
            raise ValueError("Names is required")

        if not price or price <= 0:
            raise ValueError("Price must be greater than 0")

        if quantity < 0:
            raise ValueError("Quantity must be a positive number")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None


    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion


    def get_promotion(self):
        return self.promotion


    def get_quantity(self) -> int:
        """
        Return the current quantity of the product.

        Returns:
            int: Available stock quantity.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Update the product quantity.

        Sets the new quantity value and automatically
        deactivates the product if the quantity reaches zero.

        Args:
            quantity (int): New quantity value.

        Returns:
            None
        """
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """
        Check whether the product is active.

        Returns:
            bool: True if the product is active,
                  otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activate the product.

        Marks the product as available/active.

        Returns:
            None
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.

        Marks the product as unavailable/inactive.

        Returns:
            None
        """
        self.active = False

    def show(self):

        if self.promotion:
            print(f"{self.name}, "
                  f"Price: €{self.price}, "
                  f"Quantity: {self.quantity}, "
                  f"Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}, Promotion: None")

    def buy(self, quantity: int) -> Any:

        if not self.active:
            return f'The product {self.name} is out of stock.'

        if not isinstance(quantity, int):
            raise ValueError('You must type a number')

        if quantity > self.quantity:
            raise ValueError("We cant cover this buying quantity.")
        if quantity <= 0:
            raise ValueError("Please type positive number!")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__( name, price, 0)

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Please type positive number!")

        if self.promotion:
            return self.promotion.apply_promotion(self.price,quantity)

        return quantity * self.price

    def show(self):

        if self.promotion:
            print(f"{self.name}, Price: €{self.price}, Quantity: Unlimited "
                  f"Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: €{self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f'{self.name} limited to {self.maximum} per order!')

        return quantity * self.price

    def show(self):
        print(f'{self.name}, Price: €{self.price}, Limited to {self.maximum} per order!, Promotion: None')