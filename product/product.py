class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name} - {self.description}, Price: {self.price}, Quantity: {self.quantity}"