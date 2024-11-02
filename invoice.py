class Invoice:
    """
    Invoice class represents an invoice for a completed order.

    Attributes:
        order (Order): The order associated with this invoice.
        total_with_vat (float): Total price including VAT.
    """
    VAT_RATE = 0.08  # 8% VAT

    def __init__(self, order):
        self.__order = order
        self.__total_with_vat = 0

    def calculate_VAT(self):
        """Calculates the VAT amount for the order."""
        total = self.__order.calculate_total()
        return total * self.VAT_RATE

    def generate_invoice(self):
        """Generates the invoice details."""
        total = self.__order.calculate_total()
        vat = self.calculate_VAT()
        self.__total_with_vat = total + vat
        return f"Invoice Total: ${self.__total_with_vat:.2f}, Including VAT: ${vat:.2f}"

    def __str__(self):
        """Returns a string representation of the invoice."""
        return self.generate_invoice()