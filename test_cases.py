from ebook import EBook
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from datetime import datetime

# Test Case 1: Adding E-books to Catalog
def test_ebook_management():
    ebook1 = EBook("Python Programming", "Author A", "2020-05-01", "Programming", 50.0)
    ebook2 = EBook("Data Science", "Author B", "2019-09-15", "Science", 40.0)
    print("E-book 1:", ebook1)
    print("E-book 2:", ebook2)

# Test Case 2: Creating Customer Account
def test_customer_management():
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    print("Customer:", customer)

# Test Case 3: Adding E-books to Shopping Cart
def test_shopping_cart():
    ebook1 = EBook("Python Programming", "Author A", "2020-05-01", "Programming", 50.0)
    ebook2 = EBook("Data Science", "Author B", "2019-09-15", "Science", 40.0)
    cart = ShoppingCart()
    cart.add_item(ebook1)
    cart.add_item(ebook2)
    print("Shopping Cart:", cart)
    print("Total in Cart:", cart.calculate_total())

# Test Case 4: Order with Discounts
def test_order_with_discounts():
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    order = Order(order_id=1, order_date=datetime.now(), customer=customer)
    for _ in range(5):  # Add 5 e-books to apply bulk discount
        ebook = EBook("Sample Book", "Author X", "2021-01-01", "Genre", 20.0)
        order.add_item(ebook)
    print("Order Total with Discounts:", order.calculate_total())

# Test Case 5: Generating Invoice
def test_invoice_generation():
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)
    order = Order(order_id=1, order_date=datetime.now(), customer=customer)
    order.add_item(EBook("Sample Book", "Author X", "2021-01-01", "Genre", 100.0))
    invoice = Invoice(order)
    print("Generated Invoice:", invoice)

# Running all test cases
if __name__ == "__main__":
    print("\n--- Test E-book Management ---")
    test_ebook_management()
    print("\n--- Test Customer Management ---")
    test_customer_management()
    print("\n--- Test Shopping Cart ---")
    test_shopping_cart()
    print("\n--- Test Order with Discounts ---")
    test_order_with_discounts()
    print("\n--- Test Invoice Generation ---")
    test_invoice_generation()