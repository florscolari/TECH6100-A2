
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
        self.__title: str = title
        self.__author: str = author
        self.__price: float = price
        self.__quantity: int = quantity
        self.__book_genre: BookGenre = book_genre
        self.__isbn: str = isbn
        self.__publication_year: int = publication_year
        self.__publisher: str = publisher
        self.__language: Language = language
        self.__book_format: BookFormat = book_format

    #To display data from a class object to users
    def __str__(self):
       return (f"------\n"
               f"Title: {self.__title.title()} - Author: {self.__author.title()}\n"
               f"Genre: {self.__book_genre}\n"
               f"ISBN: {self.__isbn}, Published on {self.__publication_year} by {self.__publisher}\n"
               f"Format: {self.__book_format} - Language: {self.__language}\nPrice: ${self.__price}\nAvailable:"
               f" {self.__quantity}")

    #To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Title: {self.__title}.title(): {type(self.__title)} - Author: {self.__author}.title():"
                f" {type(self.__author)}\n"
                f"Genre: {self.__book_genre}: {type(self.__book_genre)}\n"
                f"ISBN: {self.__isbn}: {type(self.__isbn)}, Published on {self.__publication_year}: {type(self.__publication_year)} by {
                self.__publisher}: {type(self.__publisher)}\n"
                f"Format: {self.__book_format}: {type(self.__book_format)} - Language: {self.__language}: "
                f"{type(self.__language)}\nPrice: ${
                self.__price}: {type(self.__price)}\nAvailable:"
                f" {self.__quantity}: {type(self.__quantity)}")


    #Book Getters
    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getPrice(self):
        return self.__price

    def getQuantity(self):
        return self.__quantity

    def getBookGenre(self):
        return self.__book_genre

    def getIsbn(self):
        return self.__isbn

    def getPublicationYear(self):
        return self.__publication_year

    def getPublisher(self):
        return self.__publisher

    def getLanguage(self):
        return self.__language

    def getBookFormat(self):
        return self.__book_format

    # Book Setters
    def setTitle(self, value):
        self.__title = value

    def setAuthor(self, value):
        self.__author = value

    def setPrice(self, value):
        self.__price = value

    def setQuantity(self, value):
        self.__quantity = value

    """Set Book Genre is handled from BookGenre class"""

    def setIsbn(self, value):
        self.__isbn = value

    def setPublicationYear(self, value):
        self.__publication_year = value

    def setPublisher(self, value):
        self.__publisher = value

    """Set Language is handled from Language class"""

    """Set Book Format is handled from BookFormat class"""



book1 = (Book("title", "John Doe", 25, 2, BookGenre.SCIFI, "1234ases", 1987, Language.ENGLISH, "Planet Editions",
         BookFormat.PAPERBACK) )
book2 = Book("title2", "author2", 45, 1, BookGenre.FICTION, "qwert1", 1988, Language.ENGLISH, "Planeta",
             BookFormat.PAPERBACK)

print(book1.getTitle())
print(book1)
book1.setAuthor("new guy")
print(book1)