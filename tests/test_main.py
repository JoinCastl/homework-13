import pytest
from category.category import Category
from product.product import Product

from typing import List


@pytest.fixture
def create_product() -> List[Product]:
    return [Product("Laptop", "High-performance laptop", 1500.50, 10),
            Product("Smartphone", "Latest smartphone model", 999.99, 20),
            Product("Tablet", "Portable tablet device", 699.99, 15)]


@pytest.fixture
def create_category(create_product: List[Product]) -> Category:
    return Category("Electronics", "Category for electronic products", create_product)


@pytest.fixture
def reset_category_counts():
    Category.total_categories = 0
    Category.total_unique_products = 0


def test_category_initialization(create_category: Category, reset_category_counts):
    assert create_category.name == "Electronics"
    assert create_category.description == "Category for electronic products"
    assert len(create_category.products) == 3
    assert Category.total_categories == 0


def test_product_initialization():
    create_product = Product("Laptop", "High-performance laptop", 1500.50, 10)
    assert create_product.name == "Laptop"
    assert create_product.description == "High-performance laptop"
    assert create_product.price == 1500.50
    assert create_product.quantity == 10


def test_create_product_and_categories(create_category: Category, reset_category_counts, create_product: List[Product]):
    assert Category.total_categories == 0
    assert Category.total_unique_products == 0

    new_product = Product("Headphones", "Premium sound quality headphones", 199.99, 30)
    create_category.add_product(new_product)

    assert len(create_product) == 4
    assert Category.total_unique_products == 1
