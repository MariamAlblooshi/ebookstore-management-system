class ShoppingCart:
    """
    ShoppingCart class represents the customer's shopping cart.

    Attributes:
        items (list): List of e-books added to the shopping cart.
    """

    def __init__(self):
        self.__items = []

    def add_item(self, ebook):
        """Adds an e-book to the shopping cart."""
        self.__items.append(ebook)

    def remove_item(self, ebook):
        """Removes an e-book from the shopping cart if it exists."""
        if ebook in self.__items:
            self.__items.remove(ebook)

    def calculate_total(self):
        """Calculates the total price of all items in the cart."""
        return sum(item.get_price() for item in self.__items)

    def __str__(self):
        """Returns a string representation of the shopping cart items."""
        return f"Shopping Cart: {[str(item) for item in self.__items]}"
