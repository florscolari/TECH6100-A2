
from enum import StrEnum



class BookGenre(StrEnum):
    """Creating set of immutable values for types of book"""
    FICTION = "Fiction"
    NONFICTION = "Non-Fiction"
    SCIFI = "Sci-Fi"
    MYSTERY = "Mystery"
    BIOGRAPHY = "Biography"

    @staticmethod
    def showAvailable():
        availableBookGenre = [BookGenre.FICTION, BookGenre.NONFICTION, BookGenre.SCIFI, BookGenre.MYSTERY, BookGenre.BIOGRAPHY]
        print("Available Book Genres:")
        for bookgenre in availableBookGenre:
            print(bookgenre)

class BookFormat(StrEnum):
    """Creating set of immutable values for book formats"""
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    EBOOK = "eBook"
    AUDIOBOOK = "Audiobook"

    @staticmethod
    def showAvailable():
        availableBookFormat = [BookFormat.HARDCOVER, BookFormat.PAPERBACK, BookFormat.EBOOK, BookFormat.AUDIOBOOK]
        print("Available Book Formats:")
        for bookformat in availableBookFormat:
            print(bookformat)


class Language(StrEnum):
    """Creating set of immutable values for the language the book is written"""
    ENGLISH = "English"
    SPANISH = "Spanish"
    PORTUGUESE = "Portuguese"
    FRENCH = "French"

    @staticmethod
    def showAvailable():
        availableLanguage = [Language.ENGLISH, Language.SPANISH, Language.PORTUGUESE, Language.FRENCH]
        print("Available Languages:")
        for lang in availableLanguage:
            print(lang)


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

    def getLanguage(self) -> Language: # Return value of type: Language
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

    """Set Book Genre if is within class BookGenre. If not -> show message"""
    def setBookGenre(self, new_book_genre: BookGenre):
        self.__book_genre = new_book_genre
        if not isinstance(new_book_genre, BookGenre):
            raise ValueError(
                "Book Genre must be one of available book genre options. Or contact the Administrator to add a new "
                "one.")

    def setIsbn(self, value):
        self.__isbn = value

    def setPublicationYear(self, value):
        self.__publication_year = value

    def setPublisher(self, value):
        self.__publisher = value

    """Set Language if is within class Language. If not -> show message"""
    def setLanguage(self, new_language: Language):
        self.__language = new_language
        if not isinstance(new_language, Language):
            raise ValueError("Language must be one of available language options. Or contact the Administrator to add a new one.")

    """Set Book Format if is within class BookFormat. If not -> show message"""
    def setBookFormat(self, new_book_format: BookFormat):
        self.__book_format = new_book_format
        if not isinstance(new_book_format, BookFormat):
            raise ValueError("Book format must be one of available book format options. Or contact the Administrator "
                             "to add a new one.")


book1 = (Book("title", "John Doe", 25, 2, BookGenre.SCIFI, "1234ases", 1987, Language.SPANISH, "Planet Editions",
         BookFormat.PAPERBACK) )
book2 = Book("title2", "author2", 45, 1, BookGenre.FICTION, "qwert1", 1988, Language.FRENCH, "Planeta",
             BookFormat.PAPERBACK)


#todo: when user input for BookGenre, BookFormat & Language -> options must be displayed, grab user selection and do
# a comparison. They can be added as direct values.

print(book1.getTitle())
print(book1)
book1.setAuthor("new guy")
book1.setLanguage(Language.FRENCH)
print(book1)
Language.showAvailable()
BookFormat.showAvailable()
BookGenre.showAvailable()
book1.setLanguage(Language.PORTUGUESE)
print(book1)
