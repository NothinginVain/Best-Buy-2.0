from products import Product

import pytest

def test_creating_normal_product():
    silver_ring = Product('Silver Ring', 100.00, 10)
    assert silver_ring.name == 'Silver Ring'
    assert silver_ring.price == 100.00
    assert silver_ring.quantity == 10
    # assert isinstance(silver_ring, Product)

def test_product_with_empty_name():
   with pytest.raises(ValueError):
        Product('', 35.00, 50)


def test_product_with_negative_price():
    with pytest.raises(ValueError):
        Product('Sonny Walkman', -35.00, 50)


def test_product_becomes_inactive():
    silver_ring = Product('Silver Ring', 100.00, 10)
    silver_ring.buy(10)
    assert silver_ring.is_active() is False

def test_product_update_quantity():
    silver_ring = Product('Silver Ring', 100.00, 10)
    silver_ring.buy(5)
    assert silver_ring.quantity == 5

def test_buying_too_much():
    silver_ring = Product('Silver Ring', 100.00, 10)
    with pytest.raises(ValueError):
        silver_ring.buy(15)


pytest.main()