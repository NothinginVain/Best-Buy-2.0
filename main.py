from products import Product, LimitedProduct, NonStockedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def list_products(store_obj):
    """List all active products in the store."""
    products_list = store_obj.get_all_products()
    print('----------------------------')
    for index, product in enumerate(products_list, start=1):
        print(f'{index}. ', end='')
        product.show()
    print('----------------------------')


def show_total(store_obj):
    """Show total quantity of all products."""
    total = store_obj.get_total_quantity()
    print(f'\nTotal of {total} items in store')


def make_order(store_obj):
    """Create an order from user input."""
    products_list = store_obj.get_all_products()

    list_products(store_obj)

    shopping_list = []

    while True:
        print('When you want to finish order, enter empty text.')
        product_pick = input('Which product # do you want? ').strip()
        if not product_pick:
            break
        try:
            selected_product = products_list[int(product_pick)-1]
            quantity_buy = int(input('What amount do you want? '))
            shopping_list.append((selected_product, quantity_buy))
            print('Product added to list!\n')
        except (ValueError, IndexError):
            print("Type the right input please")
    try:
        total_price = store_obj.order(shopping_list)
        print('**********')
        print(f'Order made! Total payment: €{total_price}')
    except ValueError as error:
        print(f'Error while making order! {error}')


def add_product(store_obj):
    """Add a new product to the store."""
    try:
        name = input("Product name: ")
        price = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))

        new_product = Product(name, price, quantity)

        store_obj.add_product(new_product)
        print(f'{name} added with success!')

    except ValueError as error:
        print(f'Could not create product: {error}')


def start(store_obj):
    """Run store menu loop."""
    menu = {
        '1': list_products,
        '2': show_total,
        '3': make_order,
        '4': add_product
    }
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Add a new product")
        print("5. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == '5':
            print('Goodbye!')
            break

        menu.get(choice, lambda _: print('Invalid input'))(store_obj)


def main():
    """Initialize store and start program."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()