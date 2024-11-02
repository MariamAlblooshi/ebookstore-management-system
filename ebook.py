class EBook:
    """
    EBook class represents an e-book in the bookstore catalog.

    Attributes:
        title (str): Title of the e-book.
        author (str): Author of the e-book.
        publication_date (str): Publication date of the e-book.
        genre (str): Genre of the e-book.
        price (float): Price of the e-book.
    """

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_price(self):
        """Returns the price of the e-book."""
        return self.__price

    def __str__(self):
        """Returns a string representation of the e-book."""
        return f"{self.__title} by {self.__author}, {self.__genre}, ${self.__price:.2f}"
