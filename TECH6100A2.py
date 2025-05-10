# TECH6100 Assessment 2 Florencia Scolari ID 1847863 May 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100-A2.git
#todo: check & complete out-of-scope features

# Out of scope: global command to cancel an ongoing task.

#PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

from enum import StrEnum


class OrderStatus(StrEnum):
    """Creating set of immutable values for order statuses"""
    NEW_ORDER = "New Order"
    PLACED = "Placed"
    CONFIRMED = "Confirmed"
    DISPATCHED = "Dispatched"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

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
        return f"{self.__street} {self.__city} {self.__state} ({self.__zip_code}) {self.__country}"


class User:
    def __init__(self, first_name, last_name, username, email, password, phone_number):
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__username : str = username
        self.__email : str = email
        self.__password : str = password
        self.__phone_number : str = phone_number
        self.__shipping_address = None #Here I found the concept of Composition
        self.__purchase_history = None  # todo: new class for this one? purchase_history (array/object)

    #To display data from a class object to users
    def __str__(self):
        if self.__shipping_address is None:
            self.__shipping_address = "-"

        if self.__purchase_history is None:
            self.__purchase_history = "-"

        return (f"------\n"
                f"Name: {self.__first_name} {self.__last_name}\n"
                f"Username: {self.__username}\n"
                f"Phone Number: {self.__phone_number}\n" #todo: placeholders to display pretty phone: +44-20-7946-0636?
                f"Shipping Address: {self.__shipping_address}\n"
                f"Purchase History: {self.__purchase_history}" #todo: count previous purchases & show details?
        )

    # To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"Name: {self.__first_name} : {type(self.__first_name)} + {self.__last_name} :"
                f" {type(self.__last_name)}\n"
                f"Username: {self.__username} : {type(self.__username)}\n"
                f"Password: {self.__password} : {type(self.__password)}\n"
                f"Phone Number: {self.__phone_number} : {type(self.__phone_number)}\n"
                f"Shipping Address: {self.__shipping_address} : {type(self.__shipping_address)}\n"
                f"Purchase History: {self.__purchase_history} : {type(self.__purchase_history)}" #todo: count
                # previous purchases &
                # show details?
        )

    #User Getters:
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_phone_number(self):
        return self.__phone_number

    def get_shipping_address(self):
        return self.__shipping_address

    def get_purchase_history(self):
        return self.__purchase_history

    # User Setters:
    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_username(self, value):
        self.__username = value

    def set_email(self, value):
        self.__email = value

    def set_password(self, value):
        self.__password = value

    def set_phone_number(self, value):
        self.__phone_number = value

    """Set Shipping Address if is within ShippingAddress class. If not -> show message"""
    def set_shipping_address(self,value):
        if isinstance(value, ShippingAddress):
            self.__shipping_address = value
        else:
            raise TypeError("The shipping address must be valid.")

    #todo: Don't think I need to set a purchase history, I need to calculate it & get it


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

#6 USERS added to have data to handle when the program starts (3 of 6 with Address)
user_list = []
user1 = User("Alice", "Nguyen", "booklover92", "alice.nguyen92@outlook.com", "A1ic3!Readz", "12025550136")
#Method to set shipping address for a user
address1 = ShippingAddress("123 Elm Street", "San Francisco", "CA", "94102", "USA")
user1.set_shipping_address(address1)
user_list.append(user1)

user2 = User("John", "Martinez", "johnny_reads", "john.martinez84@aol.co.uk", "J0hn*Reads2023", "442079460636")
address2 = ShippingAddress("45 King's Road", "London", "4RY", "SW3", "UK")
user2.set_shipping_address(address2)
user_list.append(user2)

user3 = User("Liam", "Taylor", "sci_fi_addict", "liam.taylor_sf@yahoo.com", "L!am4SciFi", "61390101234")
address3 = ShippingAddress("22 Bourke Street", "Melbourne", "VIC", "3000", "Australia")
user3.set_shipping_address(address3)
user_list.append(user3)

user4 = User("Sofia", "Lopez", "mysteryfan22", "sofia.lopez22@gmail.es", "S0fia&Mystery", "34911234567")
user_list.append(user4)

user5 = User("Michael", "Singh", "read4growth", "michael.singh.reads@example.in", "M1chael#Grow", "912240011122")
user_list.append(user5)

user6 = User("Monique", "Dubois", "momo_reads", "monique.dubois@outlook.fr", "M0nique!Books", "33123456789")
user_list.append(user6)

# Print the user list:
for user in user_list:
    print(user)


#todo: Research how to get a datetime stamp
#todo: search how to get the shipping address based on the user email
class Order:

    def __init__(self, order_id, order_date, order_status=OrderStatus.NEW_ORDER):

        self.__order_id = order_id
        self.__order_date = order_date
        self.__order_status : OrderStatus = order_status
        self.__book_list = [] #list of objects as attribute of this object // books selected by the user
        self.__total_items = 0 #it'll be calculated
        self.__total_amount = 0 #it'll be calculated
        self.__user_email = None
        self.__shipping_address = None

# todo: ORDER __str__
    def __str__(self):
        return (f"Order ID: {self.__order_id}\nCreated: {self.__order_date}\n"
                f"Status: {self.__order_status}\n"
                f"Total Price: {self.__total_amount}\t Total items: {self.__total_items}\n"
                f"Ordered by: {self.__user_email}\n"
                f"Shipping Address: {self.__shipping_address}\n"
                f"Order Details:")


    #ORDER: Getters
    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_order_status(self):
        return self.__order_status

    def get_user_id(self):
        return self.__user_email


    def get_total_items(self):
        total_items_list = []
        for book in self.__book_list:
            ind_book = book.get_title()
            total_items_list.append(ind_book)
        data = len(total_items_list)
        self.__total_items = data
        print(f"Total Book Qty: {self.__total_items}")

    def get_total_amount(self):
        price_list = []
        for book in self.__book_list:
            ind_price = book.get_price()
            price_list.append(ind_price)
        total_amount = sum(price_list)
        total_amount = round(total_amount, 2)
        print(f"Total: ${total_amount}")


    #todo: How can I know based on user email, which shipping address is correlated?
    def get_shipping_address(self):
        return self.__shipping_address

    #ORDER: Setters
    def set_order_id(self, value):
        self.__order_id = value

    def set_order_date(self, value):
        self.__order_date = value

    def set_order_status(self, new_order_status: OrderStatus):
        """Set Order status if it is within class OrderStatus. If not -> show message"""
        self.__order_status = new_order_status
        if not isinstance(new_order_status, OrderStatus):
            raise ValueError("Order status must be one of valid status options. Or contact the Administrator.")

    def set_user_id(self, value):
        self.__user_email = value


    #Other Order Methods
    def add_book_to_order(self, book: Book):
        self.__book_list.append(book)
        self.__total_items += 1

    def remove_book_from_order(self, book: Book):
        self.__book_list.remove(book)
        self.__total_items -= 1

    def display_order_items(self):
        for book in self.__book_list:
            print(f"{book.get_title()} - ${book.get_price()}")



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
order1 = Order("SKU01", "May 10th")
print(order1)
order1.add_book_to_order(book1)
order1.add_book_to_order(book2)
order1.display_order_items()
order1.get_total_amount()
order1.get_total_items()
order1.remove_book_from_order(book2)
order1.get_total_amount()
order1.get_total_items()
order1.set_order_status(OrderStatus.PLACED)
print(order1)


