from category import Category
from product import Product

# Создание объектов класса Category
category1 = Category("Electronics", "Electronic devices")

# Создание объектов класса Product
product1 = Product("Laptop", "High-performance laptop", 1200.50, 10)
product2 = Product("Smartphone", "Latest smartphone model", 800.75, 20)

# Добавление продуктов категории
category1.add_product(product1)
category1.add_product(product2)

# Вывод информации о продуктах категории
for product in category1.products:
    print(product)

print("Total categories:", Category.total_categories)
print("Total unique products:", len(Category.total_unique_products))