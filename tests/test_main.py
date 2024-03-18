import pytest
from category import Category
from product import Product

@pytest.fixture
def create_category():
    category = Category("Electronics", "Electronic devices")
    yield category
    Category.total_categories = 1

@pytest.fixture
def create_product():
    product = Product("Laptop", "Electronic devices",1200.50, 10)
    return product

def test_category_initialization(create_category):
    assert create_category.name == "Electronics"
    assert create_category.description == "Electronic devices"

def test_product_initialization(create_product):
    assert create_product.name == "Laptop"
    assert create_product.price == 1200.50
    assert create_product.quantity == 10


def test_category_count():
    assert Category.total_categories == 1
