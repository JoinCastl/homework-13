class Category:
    name: str
    description: str
    products: str
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products.add(product.name)
    def __str__(self):
        products_str = "\n".join([str(product) for product in self.products])
        return f"Category: {self.name}\nDescription: {self.description}\nProducts:\n{products_str}"
