from typing import List

from product.product import Product


class Category:
    name: str
    description: str
    products: list
    total_categories: int = 0
    total_unique_products: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

#1
     def is_product(self):
         return self.__products

#2
    #@classmethod
    #def create(cls, name, price):
        #return cls(name, price)

    #def add(self, list):
       # list.append(self)


    def __str__(self):
        products_str = "\n".join([str(product) for product in self.__products])
        return f"Category: {self.name}\nDescription: {self.description}\nProducts:\n{products_str}"

#3#def get_products(self):
   # products_list = []
    #for product in self.__products:
        #products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
    #return "\n".join(products_list)


