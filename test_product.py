from products import Product, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

import pytest


def test_creating_normal_product():
    """
    Test creation of a standard Product instance.

    Verifies that a product is correctly initialized with
    name, price, quantity, and correct type.
    """
    silver_ring = Product('Silver Ring', 100.00, 10)
    assert silver_ring.name == 'Silver Ring'
    assert silver_ring.price == 100.00
    assert silver_ring.quantity == 10
    assert isinstance(silver_ring, Product)


def test_product_with_empty_name():
    """
    Test that creating a product with an empty name raises ValueError.
    """
    with pytest.raises(ValueError):
        Product('', 35.00, 50)


def test_product_with_negative_price():
    """
    Test that creating a product with a negative price raises ValueError.
    """
    with pytest.raises(ValueError):
        Product('Sonny Walkman', -35.00, 50)


def test_product_becomes_inactive():
    """
    Test that a product becomes inactive when its quantity reaches zero.

    Buying the full stock should deactivate the product.
    """
    silver_ring = Product('Silver Ring', 100.00, 10)
    silver_ring.buy(10)
    assert silver_ring.is_active() is False


def test_product_update_quantity():
    """
    Test that product quantity updates correctly after purchase.

    Ensures that buying reduces available stock.
    """
    silver_ring = Product('Silver Ring', 100.00, 10)
    silver_ring.buy(5)
    assert silver_ring.quantity == 5


def test_buying_too_much():
    """
    Test that buying more than available stock raises ValueError.
    """
    silver_ring = Product('Silver Ring', 100.00, 10)
    with pytest.raises(ValueError):
        silver_ring.buy(15)


def test_limited_product_valid_purchase():
    """
    Test that LimitedProduct enforces maximum purchase limits.

    Ensures that buying more than allowed raises ValueError.
    """
    shipping = LimitedProduct('Shipping', 10, 250, maximum=1)

    with pytest.raises(ValueError):
        shipping.buy(2)


def test_second_half_price_promotion():
    """
    Test SecondHalfPrice promotion calculation.

    Verifies that the promotion correctly applies half price
    to every second item.
    """
    laptop = Product('Laptop', 100, 10)

    promo = SecondHalfPrice('Second Half price')
    laptop.set_promotion(promo)

    total = laptop.buy(2)

    assert total == 150


def test_third_one_free_promotion():
    """
    Test ThirdOneFree promotion calculation.

    Verifies that every third item is free in the purchase.
    """
    sunglasses = Product('SunGlasses', 100, 10)

    promo = ThirdOneFree('Third One Free!')

    sunglasses.set_promotion(promo)

    total = sunglasses.buy(3)

    assert total == 200


def test_percent_discount_promotion():
    """
    Test PercentDiscount promotion calculation.

    Verifies that a percentage discount is correctly applied
    to the total purchase price.
    """
    mac_os = Product('Mac OS', 100, 10)

    promo = PercentDiscount('50% off!', percent=50)
    mac_os.set_promotion(promo)

    total = mac_os.buy(1)

    assert total == 50


pytest.main()