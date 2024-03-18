from category import Category
from product import Product

# Создаем продукты
product1 = Product("Laptop", "High-performance laptop", 1200.50, 10)
product2 = Product("Smartphone", "Latest smartphone model", 800.75, 20)

unique_products = []

# Создаем список продуктов и категории
electronics_products = [product1, product2]
electronics_category = Category("Electronics", "Electronic devices", electronics_products)


# Для каждого продукта в списке продуктов
for product in electronics_products:
    # Если продукт еще не добавлен в список уникальных продуктов
    if product not in unique_products:
        unique_products.append(product)



total_unique_products = len(unique_products)
print("Total unique products:", total_unique_products)
print("Total categories:", Category.total_categories)
print(electronics_category)
