from abc import ABC, abstractmethod

class Product(ABC):  # Abstract base class for products
    def __init__(self, name, price, description):
        self.__name = name
        self.price = price
        self.description = description

    @abstractmethod
    def display_details(self):  # Abstract method to display product info
        pass

class Electronics(Product):
    def __init__(self, name, price, description, brand, warranty_period):
        super().__init__(name, price, description)
        self.brand = brand
        self.warranty_period = warranty_period

    def display_details(self):
        print(f"Electronics: {self.name} ({self.brand})")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")
        print(f"Warranty: {self.warranty_period} months")

class Clothing(Product):
    def __init__(self, name, price, description, size, material):
        super().__init__(name, price, description)
        self.size = size
        self.material = material

    def display_details(self):
        print(f"Clothing: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")
        print(f"Size: {self.size}, Material: {self.material}")


class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.cart = ShoppingCart()  # Customer has a shopping cart

    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)

    def view_cart(self):
        self.cart.view_items()

    def checkout(self):
        self.cart.checkout(self)  # Pass customer info for order creation
        # In a real app, you would integrate with payment gateways, etc.


class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def view_items(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for product, quantity in self.items.items():
            product.display_details()
            print(f"Quantity: {quantity}")
            print("-" * 20)

    def checkout(self, customer):  # Create an order
        if not self.items:
            print("Cannot checkout an empty cart.")
            return

        order = Order(customer, self.items)
        order.calculate_total()
        order.display_order_details()
        self.items = {}  # Clear the cart after checkout
        print("Thank you for your order!")


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items  # {product: quantity}
        self.total = 0

    def calculate_total(self):
        for product, quantity in self.items.items():
            self.total += product.price * quantity

    def display_order_details(self):
        print("Order Details:")
        print(f"Customer: {self.customer.name}")
        for product, quantity in self.items.items():
            product.display_details()
            print(f"Quantity: {quantity}")
        print(f"Total: ${self.total}")


# Example Usage:

phone = Electronics("Smartphone X", 799, "High-end phone", "BrandA", 24)
tshirt = Clothing("Casual T-shirt", 25, "Cotton t-shirt", "M", "Cotton")

customer1 = Customer("Alice", "123 Main St", "alice@example.com")
customer1.add_to_cart(phone)
customer1.add_to_cart(tshirt, 2)

customer1.view_cart()
customer1.checkout()


customer2 = Customer("Bob", "456 Oak Ave", "bob@example.com")  # Another customer
customer2.add_to_cart(phone)  # Bob adds the same phone
customer2.checkout()  #  Bob checkouts