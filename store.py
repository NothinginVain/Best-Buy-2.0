from products import Product


class Store:
    """
    Represent a store that manages a collection of products.

    Provides functionality to add or remove products,
    retrieve inventory information, and process customer
    orders.
    """

    def __init__(self, product_list: list):
        """
        Initialize a Store instance.

        Args:
            product_list (list): A list of Product objects
                                 available in the store.
        """
        self.product_list = product_list

    def add_product(self, product: Product):
        """
        Add a product to the store inventory.

        Args:
            product (Product): Product object to add.

        Returns:
            None
        """
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store inventory.

        Args:
            product (Product): Product object to remove.

        Returns:
            None
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in stock.

        Returns:
            int: Sum of quantities for all products in the store.
        """
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> list[Product]:
        """
        Retrieve all active products in the store.

        Filters the inventory and returns only products
        currently marked as active.

        Returns:
            list[Product]: List of active Product objects.
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Process a customer order.

        Iterates through a shopping list, purchases the
        requested quantities, and calculates the total cost.

        Args:
            shopping_list (list[tuple]): List of tuples where:
                - First element is a Product object.
                - Second element is the quantity to purchase.

        Returns:
            float: Total cost of the order.

        Raises:
            ValueError: Propagated from Product.buy() if
                        requested quantity is invalid or
                        exceeds available stock.
        """
        total_order = 0
        for item, quantity in shopping_list:
            total_order += item.buy(quantity)
        return float(total_order)