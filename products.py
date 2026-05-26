class Product:
    """
    Represent a product in inventory.

    Stores product details such as name, price, quantity,
    and active status. Provides methods to manage stock,
    activation state, and product purchases.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a Product instance.

        Validates the provided name, price, and quantity
        before creating the product object.

        Args:
            name (str): Name of the product.
            price (float): Price of the product. Must be greater than 0.
            quantity (int): Available quantity in stock.
                            Must be zero or greater.

        Raises:
            ValueError:
                - If name is empty.
                - If price is less than or equal to 0.
                - If quantity is negative.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Names is required")

        if not price or price <= 0:
            raise ValueError("Price must be above 0")

        if not quantity or quantity < 0:
            raise ValueError("Quantity must be a positive number")
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
        except ValueError as e:
            print(e)
        self.active = True

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
        self.quantity = quantity

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
        """
        Display product information.

        Prints the product name, price, and available quantity.

        Returns:
            None
        """
        print(f"{self.name}, Price: €{self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Process a product purchase.

        Reduces the available stock by the purchased quantity.
        Automatically deactivates the product if stock reaches zero.

        Args:
            quantity (int): Number of items being purchased.

        Returns:
            float: Total purchase cost.

        Raises:
            ValueError:
                - If requested quantity exceeds available stock.
                - If quantity is less than or equal to zero.
        """
        if quantity > self.quantity:
            raise ValueError("We cant cover this buying quantity.")
        if quantity <= 0:
            raise ValueError("Please type positive number!")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price