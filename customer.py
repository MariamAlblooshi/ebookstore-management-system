class Customer:
    """
    Customer class represents a customer of the bookstore.

    Attributes:
        name (str): Name of the customer.
        contact_info (str): Contact information of the customer.
        is_loyalty_member (bool): Indicates if the customer is a loyalty program member.
    """

    def __init__(self, name, contact_info, is_loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member

    def is_loyal_member(self):
        """Returns True if the customer is a loyalty program member, False otherwise."""
        return self.__is_loyalty_member

    def __str__(self):
        """Returns a string representation of the customer."""
        return f"Customer: {self.__name}, Loyalty Member: {'Yes' if self.__is_loyalty_member else 'No'}"