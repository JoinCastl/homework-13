class Category:
    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_unique_products.add(name)

category1 = Category("Electronics", "Category for electronic products")
product1 = Product("Laptop", "High performance laptop", 1500, 10)
product2 = Product("Smartphone", "Latest smartphone model", 800, 20)

category2 = Category("Clothing", "Category for clothing items")
product3 = Product("T-shirt", "Basic cotton t-shirt", 20, 50)

for product in Category.total_unique_products:
    print(f"Unique Product: {product}")

print(f"Total Categories: {Category.total_categories}")
