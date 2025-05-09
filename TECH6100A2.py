# TECH6100 Assessment 2 Florencia Scolari ID 1847863 May 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100-A2.git
#todo: check & complete out-of-scope features

# Out of scope: global command to cancel an ongoing task.

#PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

from enum import StrEnum

class BookGenre(StrEnum):
    """Creating set of immutable values for types of book"""
    FICTION = "Fiction"
    NONFICTION = "Non-Fiction"
    SCIFI = "Sci-Fi"
    MYSTERY = "Mystery"
    BIOGRAPHY = "Biography"

    @staticmethod
    def show_available():
        available_book_genre = [BookGenre.FICTION, BookGenre.NONFICTION, BookGenre.SCIFI, BookGenre.MYSTERY, BookGenre.BIOGRAPHY]
        print("Available Book Genres:")
        for genre in available_book_genre:
            print(genre)

class BookFormat(StrEnum):
    """Creating set of immutable values for book formats"""
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    EBOOK = "eBook"
    AUDIOBOOK = "Audiobook"

    @staticmethod
    def show_available():
        available_book_format = [BookFormat.HARDCOVER, BookFormat.PAPERBACK, BookFormat.EBOOK, BookFormat.AUDIOBOOK]
        print("Available Book Formats:")
        for bformat in available_book_format:
            print(bformat)


class Language(StrEnum):
    """Creating set of immutable values for the language the book is written"""
    ENGLISH = "English"
    SPANISH = "Spanish"
    PORTUGUESE = "Portuguese"
    FRENCH = "French"

    @staticmethod
    def show_available():
        available_language = [Language.ENGLISH, Language.SPANISH, Language.PORTUGUESE, Language.FRENCH]
        print("Available Languages:")
        for lang in available_language:
            print(lang)


class Book:
    def __init__(self, title, author, price, quantity, book_genre: BookGenre, isbn, publication_year,
                 language: Language,
                 publisher,
                 book_format: BookFormat):
        self.__title : str = title
        self.__author : str = author
        self.__price : float = price
        self.__quantity : int = quantity
        self.__book_genre : BookGenre = book_genre
        self.__isbn : str = isbn
        self.__publication_year : int = publication_year
        self.__publisher : str = publisher
        self.__language : Language = language
        self.__book_format : BookFormat = book_format

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
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_book_genre(self):
        return self.__book_genre

    def get_isbn(self):
        return self.__isbn

    def get_publication_year(self):
        return self.__publication_year

    def get_publisher(self):
        return self.__publisher

    def get_language(self) -> Language: # Return value of type: Language
        return self.__language

    def get_book_format(self):
        return self.__book_format

    # Book Setters
    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value

    def set_price(self, value):
        self.__price = value

    def set_quantity(self, value):
        self.__quantity = value

    """Set Book Genre if is within class BookGenre. If not -> show message"""
    def set_book_genre(self, new_book_genre: BookGenre):
        self.__book_genre = new_book_genre
        if not isinstance(new_book_genre, BookGenre):
            raise ValueError(
                "Book Genre must be one of available book genre options. Or contact the Administrator to add a new "
                "one.")

    def set_isbn(self, value):
        self.__isbn = value

    def set_publication_year(self, value):
        self.__publication_year = value

    def set_publisher(self, value):
        self.__publisher = value

    """Set Language if is within class Language. If not -> show message"""
    def set_language(self, new_language: Language):
        self.__language = new_language
        if not isinstance(new_language, Language):
            raise ValueError("Language must be one of available language options. Or contact the Administrator to add a new one.")

    """Set Book Format if is within class BookFormat. If not -> show message"""
    def set_book_format(self, new_book_format: BookFormat):
        self.__book_format = new_book_format
        if not isinstance(new_book_format, BookFormat):
            raise ValueError("Book format must be one of available book format options. Or contact the Administrator "
                             "to add a new one.")


class ShippingAddress:
    def __init__(self, street, city, state, postal_code, country):
        self.__street: str = street
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: str = postal_code
        self.__country: str = country

    def __str__(self):
        return f"{self.__street} {self.__city} {self.__state} ({self.__zip_code}) {self.__country}\n"


class User:
    def __init__(self, first_name, last_name, username, email, password, phone_number):
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__username : str = username
        self.__email : str = email
        self.__password : str = password
        self.__phone_number : str = phone_number
        self.shipping_address = None #Here I found the concept of Composition
        self.__purchase_history = None  # todo: new class for this one? purchase_history (array/object)

    #To display data from a class object to users
    def __str__(self):
        return (f"------\n"
                f"Username: {self.__username}\n"
                f"Password: {self.__password}\n"
                f"Name: {self.__first_name} {self.__last_name}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Shipping Address: {self.shipping_address}\n"
                f"Purchase History:\n {self.__purchase_history}" #todo: count previous purchases & show details?
        )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Username: {self.__username} : {type(self.__username)}\n"
                f"Password: {self.__password} : {type(self.__password)}\n"
                f"Name: {self.__first_name} : {type(self.__first_name)} + {self.__last_name} :"
                f" {type(self.__last_name)}\n"
                f"Phone Number: {self.__phone_number} : {type(self.__phone_number)}\n"
                f"Shipping Address: {self.__shipping_address} : {type(self.__shipping_address)}\n"
                f"Purchase History:\n {self.__purchase_history} : {type(self.__purchase_history)}" #todo: count previous purchases &
                # show details?
        )

#6 BOOKS added to have data to handle when the program starts
book1 = (Book("Dune", "Frank Herbert", 14.99, 8, BookGenre.SCIFI, "9780441172719", 1965, Language.ENGLISH, "Chilton Books",
         BookFormat.PAPERBACK) )
book2 = Book("The Martian", "Andy Weir", 12.50, 4, BookGenre.SCIFI, "9780804139021", 2014, Language.ENGLISH, "Crown Publishing Group",
             BookFormat.HARDCOVER)
book3 = Book("The Girl with the Dragon Tattoo", "Stieg Larsson", 11.99, 5, BookGenre.MYSTERY, "9780307949486", 2005, Language.FRENCH, "Norstedts Förlag",
             BookFormat.HARDCOVER)
book4 = Book("Gone Girl", "Gillian Flynn", 10.99, 8, BookGenre.MYSTERY, "9780307588371", 2012, Language.PORTUGUESE, "Crown Publishing Group",
             BookFormat.PAPERBACK)
book5 = Book("Steve Jobs", "Walter Isaacson", 18, 16, BookGenre.BIOGRAPHY, "9781451648539", 2011, Language.SPANISH, "Simon & Schuster",
             BookFormat.EBOOK)
book6 = Book("Becoming", "Michelle Obama", 16.99, 12, BookGenre.BIOGRAPHY, "9781524763138", 2018, Language.ENGLISH, "Crown Publishing Group",
             BookFormat.HARDCOVER)

#6 USERS added to have data to handle when the program starts
user1 = User("Flor", "Scolari", "fscolari", "fscolari@gmail.com", "FSbooks!12", "415851000")
print(user1)
user1.shipping_address = ShippingAddress("123 Elm Street", "San Francisco", "CA", "94102", "USA")
print(user1)
# todo: USER: getters for 8 attributes above (6 easy, 2 to investigate)

#todo: USER: setters for 8 attributes above (6 easy, 2 to investigate)


#todo: write ORDER class & attributes

# todo: ORDER __str__
# todo: ORDER __repr__

# todo: ORDER: getters for 8? attributes above

# todo: ORDER: setters for 8? attributes above





#todo: when user input for BookGenre, BookFormat & Language -> options must be displayed, grab user selection and do
# a comparison. They can be added as direct values.

print(book1.get_title())
print(book1)
book1.set_author("new guy")
book1.set_language(Language.FRENCH)
print(book1)
Language.show_available()
BookFormat.show_available()
BookGenre.show_available()
book1.set_language(Language.PORTUGUESE)
print(book1)
