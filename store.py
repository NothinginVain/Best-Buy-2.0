from products import Product


class Store:
    """
    Store that manages a collection of products and orders.
    """

    def __init__(self, product_list: list):
        """
        Initialize store with a list of products.

        Args:
            product_list (list): List of Product objects.
        """
        self.product_list = product_list

    def add_product(self, product: Product):
        """
        Add a product to inventory.

        Args:
            product (Product): Product to add.
        """
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from inventory.

        Args:
            product (Product): Product to remove.
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Return total quantity of all products.

        Returns:
            int: Total stock quantity.
        """
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> list[Product]:
        """
        Return all active products.

        Returns:
            list[Product]: Active products only.
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Process an order and return total price.

        Args:
            shopping_list (list[tuple]): (Product, quantity) pairs.

        Returns:
            float: Total order cost.
        """
        total_order = 0
        for item, quantity in shopping_list:
            total_order += item.buy(quantity)
        return float(total_order)