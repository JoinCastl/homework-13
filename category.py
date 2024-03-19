from typing import List
class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)


    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products += 1

