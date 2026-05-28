from promotions import Promotion
from typing import Optional, Any


class Product:
    """
    Represent a product in the store with optional promotion support.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a Product instance with validation.

        Args:
            name (str): Product name.
            price (float): Product price (> 0).
            quantity (int): Available stock (>= 0).

        Raises:
            ValueError: If input values are invalid.
        """
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
        """Assign a promotion to the product."""
        self.promotion = promotion

    def get_promotion(self):
        """Return assigned promotion."""
        return self.promotion

    def get_quantity(self) -> int:
        """
        Return current stock quantity.

        Returns:
            int: Available quantity.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Update product quantity and activation state.

        Args:
            quantity (int): New stock quantity.

        Raises:
            ValueError: If quantity is negative.
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
        Check if product is active.

        Returns:
            bool: True if active, otherwise False.
        """
        return self.active

    def activate(self):
        """Activate product."""
        self.active = True

    def deactivate(self):
        """Deactivate product."""
        self.active = False

    def show(self):
        """Print product details."""
        if self.promotion:
            print(f"{self.name}, "
                  f"Price: €{self.price}, "
                  f"Quantity: {self.quantity}, "
                  f"Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: €{self.price}, "
                  f"Quantity: {self.quantity}, Promotion: None")

    def buy(self, quantity: int) -> Any:
        """
        Purchase product and return total price.

        Args:
            quantity (int): Number of items to buy.

        Returns:
            float | str: Total price or message if unavailable.

        Raises:
            ValueError: If quantity is invalid or exceeds stock.
        """
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
    """
    Product type with unlimited stock (e.g. digital goods).
    """

    def __init__(self, name: str, price: float):
        """
        Initialize a non-stocked product.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        super().__init__(name, price, 0)

    def buy(self, quantity: int) -> float:
        """
        Purchase unlimited stock product.

        Args:
            quantity (int): Quantity to buy.

        Returns:
            float: Total price.

        Raises:
            ValueError: If quantity is invalid.
        """
        if quantity <= 0:
            raise ValueError("Please type positive number!")

        if self.promotion:
            return self.promotion.apply_promotion(self.price, quantity)

        return quantity * self.price

    def show(self):
        """Print product details (unlimited stock)."""
        if self.promotion:
            print(f"{self.name}, Price: €{self.price}, Quantity: Unlimited "
                  f"Promotion: {self.promotion.name}")
        else:
            print(f"{self.name}, Price: €{self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    """
    Product with a maximum purchase limit per order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initialize a limited product.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Stock quantity.
            maximum (int): Max units allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Purchase limited product within allowed quantity.

        Args:
            quantity (int): Quantity to buy.

        Returns:
            float: Total price.

        Raises:
            ValueError: If quantity exceeds allowed limit.
        """
        if quantity > self.maximum:
            raise ValueError(f'{self.name} limited to {self.maximum} per order!')

        return quantity * self.price

    def show(self):
        """Print limited product info."""
        print(f'{self.name}, Price: €{self.price}, Limited to '
              f'{self.maximum} per order!, Promotion: None')