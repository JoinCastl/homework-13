import pytest

from main import Category, Product

@pytest.fixture
def sample_category():
    return Category("Electronics", "Category for electronic products")

@pytest.fixture
def sample_product():
    return Product("Laptop", "High performance laptop", 1500, 10)

def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Category for electronic products"

def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High performance laptop"
    assert sample_product.price == 1500
    assert sample_product.quantity == 10

def test_count_products(sample_category):
    assert len(sample_category.products) == 0
    product1 = Product("Smartphone", "Latest smartphone model", 800, 20)
    sample_category.products.append(product1)
    assert len(sample_category.products) == 1

def test_count_categories():
    initial_categories = Category.total_categories
    category1 = Category("Clothing", "Category for clothing items")
    category2 = Category("Furniture", "Category for home furniture")
    assert Category.total_categories == initial_categories + 2

def test_count_unique_products(sample_product):
    initial_unique_products = len(Category.total_unique_products)
    product2 = Product("Smartwatch", "Fitness smartwatch", 200, 15)
    assert len(Category.total_unique_products) == initial_unique_products + 1