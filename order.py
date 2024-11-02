from datetime import datetime


class Order:
    """
    Order class represents an order placed by a customer.

    Attributes:
        order_id (int): Unique identifier for the order.
        order_date (datetime): Date the order was placed.
        customer (Customer): Customer who placed the order.
        items (list): List of e-books in the order.
        total_price (float): Total price after discounts.
    """

    def __init__(self, order_id, order_date, customer):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__customer = customer
        self.__items = []
        self.__total_price = 0

    def add_item(self, ebook):
        """Adds an e-book to the order."""
        self.__items.append(ebook)

    def apply_discount(self):
        """Applies discounts based on loyalty membership and bulk purchase."""
        if self.__customer.is_loyal_member():
            self.__total_price *= 0.9  # Loyalty discount
        if len(self.__items) >= 5:
            self.__total_price *= 0.8  # Bulk purchase discount

    def calculate_total(self):
        """Calculates the total price of the order after discounts."""
        self.__total_price = sum(item.get_price() for item in self.__items)
        self.apply_discount()
        return self.__total_price

    def __str__(self):
        """Returns a string representation of the order."""
        return f"Order ID: {self.__order_id}, Total: ${self.calculate_total():.2f}" 