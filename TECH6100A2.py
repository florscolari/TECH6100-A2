#todo: Create Book class
class Book:
    def __init__(self, title, author, price, quantity, book_type, isbn, publication_date, language, publisher,
                 book_format):
        self.title: str = title
        self.author: str = author
        self.price: float = price
        self.quantity: int = quantity
        self.book_type: str = book_type
        self.isbn: str = isbn
        self.publication_date: str = publication_date
        self.publisher: str = publisher
        self.language: str = language
        self.book_format: str = book_format
#todo: Book Attributes x10

#todo: Use Enum class for list of constant values (genre, format, language)

#todo: constructor init & repr

