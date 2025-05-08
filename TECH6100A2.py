
from enum import StrEnum

class BookGenre(StrEnum):
    """Creating set of immutable values for types of book"""
    FICTION = "Fiction"
    NONFICTION = "Non-Fiction"
    SCIFI = "Sci-Fi"
    MYSTERY = "Mystery"
    BIOGRAPHY = "Biography"

#todo: BookGenre getters

#todo: BookGenre setters


class BookFormat(StrEnum):
    """Creating set of immutable values for book formats"""
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    EBOOK = "eBook"
    AUDIOBOOK = "Audiobook"
#todo: BookFormat getters

#todo: BookFormat setters

class Language(StrEnum):
    """Creating set of immutable values for the language the book is written"""
    ENGLISH = "English"
    SPANISH = "Spanish"
    PORTUGUESE = "Portuguese"
    FRENCH = "French"
#todo: Language getters

#todo: Language setters

class Book:
    def __init__(self, title, author, price, quantity, book_genre: BookGenre, isbn, publication_year,
                 language: Language,
                 publisher,
                 book_format: BookFormat):
        self.title: str = title
        self.author: str = author
        self.price: float = price
        self.quantity: int = quantity
        self.book_genre: BookGenre = book_genre
        self.isbn: str = isbn
        self.publication_year: int = publication_year
        self.publisher: str = publisher
        self.language: Language = language
        self.book_format: BookFormat = book_format

    #To display data from a class object to users
    def __str__(self):
       return (f"------\n"
               f"Title: {self.title.title()} - Author: {self.author.title()}\n"
               f"Genre: {self.book_genre}\n"
               f"ISBN: {self.isbn}, Published on {self.publication_year} by {self.publisher}\n"
               f"Format: {self.book_format} - Language: {self.language}\nPrice: ${self.price}\nAvailable:"
               f" {self.quantity}")

    #To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Title: {self.title}.title(): {type(self.title)} - Author: {self.author}.title():"
                f" {type(self.author)}\n"
                f"Genre: {self.book_genre}: {type(self.book_genre)}\n"
                f"ISBN: {self.isbn}: {type(self.isbn)}, Published on {self.publication_year}: {type(self.publication_year)} by {
                self.publisher}: {type(self.publisher)}\n"
                f"Format: {self.book_format}: {type(self.book_format)} - Language: {self.language}: "
                f"{type(self.language)}\nPrice: ${
                self.price}: {type(self.price)}\nAvailable:"
                f" {self.quantity}: {type(self.quantity)}")


#todo: Book getters

#todo: Book setters


book1 = (Book("title", "John Doe", 25, 2, BookGenre.SCIFI, "1234ases", 1987, Language.ENGLISH, "Planet Editions",
         BookFormat.PAPERBACK) )
book2 = Book("title2", "author2", 45, 1, BookGenre.FICTION, "qwert1", 1988, Language.ENGLISH, "Planeta",
             BookFormat.PAPERBACK)
