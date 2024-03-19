from typing import List

from product.product import Product


class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0

    def __init__(self, name: str, description: str, products: List['Product']):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products += 1

    def __str__(self):
        products_str = "\n".join([str(product) for product in self.products])
        return f"Category: {self.name}\nDescription: {self.description}\nProducts:\n{products_str}"


def get_total_unique_products():
    return len(Category.total_unique_products)
