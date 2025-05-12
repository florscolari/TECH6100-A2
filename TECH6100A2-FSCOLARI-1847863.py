# TECH6100 Assessment 2 Florencia Scolari ID 1847863 May 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100-A2.git

# User for Testing Purposes:
# First Name: Elle
# Last Name: Test
# Username: test2025
# Email: test@t.com.au
# Password: 123
# Order ID: 0011122

# Out of scope:
# 1. Global command to cancel an ongoing task.
# 2. No user input validation for: phone, email & shipping address.
# 3. Turning back for case: If user selects she/he has an account and doesn't know username & password, no way to recover from that. Dead End.
# 4. Login as different user types at tge beginning. You can create account & login to place an order.
# 5. Although I have set __str__ & __repr__ for Book, Order & User, I've used __str__ in most cases instead of __repr__


# PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

from datetime import datetime
from enum import StrEnum


# ------ START 🙋‍♀️ USER Classes --------- #
class User:
    def __init__(self, first_name, last_name, username, email, password, phone_number):
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__username : str = username
        self.__email : str = email
        self.__password : str = password
        self.__phone_number : str = phone_number
        self.__shipping_address = None #Here I found the concept of Composition
        self.__order_history = []  #list of Order objects as Purchase History

    #To display data from a class object to users
    def __str__(self):
        order_list_str = "\n".join([f"- ID: {order.get_order_id()}\tItems: {order.get_total_items()}\tAmount: $"
                                    f"{order.get_total_amount()}\tDate:"
                                    f" {order.get_order_date()}"
                                    for order in self.__order_history])
        return (f"# --------------- #\n"
                f"Name: {self.__first_name.title()} {self.__last_name.title()}\n"
                f"Username: {self.__username}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n"
                f"Shipping Address: {self.__shipping_address}\n"
                f"Purchase History: {len(self.__order_history)} orders\n"
                f"{order_list_str}\n"
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
                f"Purchase History: {self.__order_history} : {type(self.__order_history)}"
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

    def get_order_history(self):
        return self.__order_history

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

    def add_order(self, uorder):
        self.__order_history.append(uorder)


    """Set Shipping Address if is within ShippingAddress class. If not -> show message"""
    def set_shipping_address(self,value):
        if isinstance(value, ShippingAddress):
            self.__shipping_address = value
        else:
            raise TypeError("The shipping address must be valid.")

class ShippingAddress:
    def __init__(self, street, city, state, postal_code, country):
        self.__street: str = street
        self.__city: str = city
        self.__state: str = state
        self.__zip_code: str = postal_code
        self.__country: str = country

    def __str__(self):
        return (f"{self.__street.title()} {self.__city.title()} {self.__state.upper()} ({self.__zip_code})"
                f" {self.__country.title()}")


class UserInventory:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__total_users = 0
        self.__email_list = []
        self.__username_list = []
        self.__password_list = []

    #Getters
    def get_user_list(self):
        return self.__user_list

    def get_email_list(self):
        self.__email_list = []
        for user in self.__user_list:
            self.__email_list.append(user.get_email())
        return self.__email_list

    def get_username_list(self):
        self.__username_list = []
        for user in self.__user_list:
            self.__username_list.append(user.get_username())
        return self.__username_list

    def get_password_list(self):
        self.__password_list = []
        for user in self.__user_list:
            self.__password_list.append(user.get_password())
        return self.__password_list

    def __str__(self):
        return (f"🙋‍♀️️  {self.__name}  🙋‍♀️\n\t"
                f"Current users: {self.__total_users}\n")

    def display_user_list(self):
        for user in self.__user_list:
            print(f"{user.__str__()}")

    def add_user(self, user: User):
        self.__user_list.append(user)
        self.__total_users += 1

    def remove_user(self, user: User):
        self.__user_list.remove(user)
        self.__total_users -= 1

# ------ END 🙋‍♀️ USER Classes --------- #

# ------ START 🛍️ ORDER Classes --------- #
class OrderStatus(StrEnum):
    """Creating set of immutable values for order statuses"""
    NEW_ORDER = "New Order"
    PLACED = "Placed"
    CONFIRMED = "Confirmed"
    DISPATCHED = "Dispatched"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

class Order:
    """switching approaches: this will take the whole User object as argument to create an Order object,
    not only user_email"""
    def __init__(self, order_id, user, order_status=OrderStatus.NEW_ORDER):
        timestamp = datetime.now()
        self.__order_id = order_id
        self.__order_date = timestamp.strftime("%a %d %b %H:%M")
        self.__order_status : OrderStatus = order_status
        self.__book_list = [] #list of objects as attribute of this object // books selected by the user
        self.__total_items = 0
        self.__total_amount = 0 #it'll be calculated
        self.__user: User = user #This is the entire User object

    def __str__(self):
        book_list_str = "\n".join([f"- {book.display_book_short_details()}" for book in self.__book_list])
        return (f"# --------------- #\n"
                f"Order ID: {self.__order_id}\nCreated: {self.__order_date}\n"
                f"Status: {self.__order_status}\n"
                f"Total Amount: ${round(self.__total_amount, 2)}\n"
                f"Total items: {self.__total_items}\n"
                f"Ordered by: {self.__user.get_email()}\n"
                f"Shipping Address: {self.__user.get_shipping_address()}\n"
                f"Order Details:\n{book_list_str}\n")

    #ORDER: Getters
    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_order_status(self):
        return self.__order_status

    def get_user_id(self):
        return self.__user.get_email()

    def get_total_items(self):
        return self.__total_items

    def get_total_amount(self):
        return round(self.__total_amount, 2)

    def get_book_list(self):
        return self.__book_list

    def get_shipping_address(self):
        return self.__user.get_shipping_address()

    #ORDER: Setters
    def set_order_id(self, value):
        self.__order_id = value

    def set_order_date(self, value):
        self.__order_date = value

    def set_user(self, user):
        self.__user = user

    def set_order_status(self, new_order_status: OrderStatus):
        """Set Order status if it is within class OrderStatus. If not -> show message"""
        self.__order_status = new_order_status
        if not isinstance(new_order_status, OrderStatus):
            raise ValueError("Order status must be one of valid status options. Or contact the Administrator.")


    #Other Order Methods
    def add_book_to_order(self, book):
        self.__book_list.append(book)
        self.__total_items = len(self.__book_list)
        self.__total_amount += book.get_price()

    def remove_book_from_order(self, book):
        self.__book_list.remove(book)
        self.__total_items = len(self.__book_list)
        self.__total_amount -= book.get_price()


    def display_order_items(self):
        for book in self.__book_list:
            print(f"{book.get_title()} - ${book.get_price()}")

    def display_order_summary(self):
        print(f"🛍️ Your Shopping cart:\n"
                f"\tItems: {self.__total_items}\n"
                f"\tTotal: ${round(self.__total_amount,2)}")
        for book in self.__book_list:
            print(f"\t{book.get_book_id()} {book.get_title()} - ${book.get_price()}")

class OrderInventory:
    def __init__(self, name):
        self.__name = name
        self.__order_list = []
        self.__total_orders = 0
        self.__total_sells = 0
        self.__total_items_sold = 0

    def __str__(self):
        return (f"🛍️  {self.__name}  🛍️\n\tTotal Qty Orders: {self.__total_orders}\n\tTotal Books sold:"
                f" {self.__total_items_sold}\n\tTotal Sold: ${round(self.__total_sells, 2)}\n")

    def display_order_list(self):
        for order in self.__order_list:
            print(f"{order.__str__()}")

    def get_order_list(self):
        return self.__order_list

    def add_order(self, order: Order):
        self.__order_list.append(order)
        self.__total_orders += 1
        self.__total_sells += order.get_total_amount()
        self.__total_items_sold += order.get_total_items()

    def remove_order(self, order: Order):
        self.__order_list.remove(order)
        self.__total_orders -= 1
        self.__total_sells -= order.get_total_amount()
        self.__total_items_sold -= order.get_total_items()


# ------ START 📚 BOOK Classes --------- #

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
    def __init__(self, book_id, title, author, price, quantity, book_genre: BookGenre, isbn, publication_year,
                 language: Language,
                 publisher,
                 book_format: BookFormat):
        self.__book_id : str = book_id
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
       return (f"# --------------- #\n"
               f"ID: {self.__book_id}\n"
               f"Title: {self.__title.title()} - Author: {self.__author.title()}\n"
               f"Genre: {self.__book_genre}\n"
               f"ISBN: {self.__isbn}, Published on {self.__publication_year} by {self.__publisher}\n"
               f"Format: {self.__book_format} - Language: {self.__language}\nPrice: ${self.__price}\nAvailable:"
               f" {self.__quantity}\n")

    #To display data from a class object to programmers
    def __repr__(self):
        return (f"------\n"
                f"ID: {self.__book_id}\n"
               f"Title: {self.__title.title()} - Author: {self.__author.title()}\n"
               f"Genre: {self.__book_genre}\n"
               f"ISBN: {self.__isbn}, Published on {self.__publication_year} by {self.__publisher}\n"
               f"Format: {self.__book_format} - Language: {self.__language}\nPrice: ${self.__price}\n"
               f"Available: {self.__quantity}")


    #Book Getters
    def get_book_id(self):
        return self.__book_id

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

    def display_book_short_details(self):
        return f"{self.get_book_id()}\t{self.get_title()}\t${self.get_price()}"

    # Book Setters
    def set_book_id(self, value):
        self.__book_id = value

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


class BookInventory:
    def __init__(self, name):
        self.__name = name
        self.__book_list = []
        self.__total_books = 0
        self.__book_id_list = []

    def __str__(self):
        return (f"📚️  {self.__name}  📚\n\t"
                f"Total Qty Books: {self.__total_books}\n")

    #Getters
    def get_book_list(self):
        return self.__book_list

    def get_book_id_list(self):
        self.__book_id_list = []
        for book in self.__book_list:
            self.__book_id_list.append(book.get_book_id())
        return self.__book_id_list

    def get_total_books(self):
        return self.__total_books

    def display_book_list(self):
        for book in self.__book_list:
            print(f"{book.__str__()}")

    def display_short_book_list(self):
        for book in self.__book_list:
            print(f"{book.get_book_id()}\t{book.get_title()}\t${book.get_price()}\t Available: {book.get_quantity()}")

    def add_book(self, book: Book):
        self.__book_list.append(book)
        self.__total_books += book.get_quantity()

    def remove_book(self, book: Book):
        self.__book_list.remove(book)
        self.__total_books -= book.get_quantity()

    def updatePlus1_book_list(self):
        self.__total_books += 1

    def updateMinus1_book_list(self):
        self.__total_books -= 1

    def subtract_order_book(self, order: Order):
        self.__total_books -= order.get_total_items()

# ------ END 📚 BOOK Classes --------- #



# ------ END 🛍️ ORDER Classes --------- #
#7 USERS added to have data to handle when the program starts
user_list = UserInventory("User Collection")

#Recommend to use 1st user for testing purposes
user0 = User("Elle", "Test", "test2025", "test@t.com.au", "123", "00000000000")
#Method to set shipping address for a user
address0 = ShippingAddress("000 William Street", "Perth", "WA", "6000", "Australia")
user0.set_shipping_address(address0)
user_list.add_user(user0)

user1 = User("Alice", "Nguyen", "booklover92", "alice.nguyen92@outlook.com", "A1ic3!Readz", "12025550136")
#Method to set shipping address for a user
address1 = ShippingAddress("123 Elm Street", "San Francisco", "CA", "94102", "USA")
user1.set_shipping_address(address1)
user_list.add_user(user1)

user2 = User("John", "Martinez", "johnny_reads", "john.martinez84@aol.co.uk", "J0hn*Reads2023", "442079460636")
address2 = ShippingAddress("45 King's Road", "London", "4RY", "SW3", "UK")
user2.set_shipping_address(address2)
user_list.add_user(user2)

user3 = User("Liam", "Taylor", "sci_fi_addict", "liam.taylor_sf@yahoo.com", "L!am4SciFi", "61390101234")
address3 = ShippingAddress("22 Bourke Street", "Melbourne", "VIC", "3000", "Australia")
user3.set_shipping_address(address3)
user_list.add_user(user3)

user4 = User("Sofia", "Lopez", "mysteryfan22", "sofia.lopez22@gmail.es", "S0fia&Mystery", "34911234567")
address4 = ShippingAddress("Calle Gran Vía 12", "Madrid", "MD", "28013", "Spain")
user4.set_shipping_address(address4)
user_list.add_user(user4)

user5 = User("Michael", "Singh", "read4growth", "michael.singh.reads@example.in", "M1chael#Grow", "912240011122")
address5 = ShippingAddress("501 Bandra Kurla Complex", "Mumbai", "MH", "400051", "India")
user5.set_shipping_address(address5)
user_list.add_user(user5)

user6 = User("Monique", "Dubois", "momo_reads", "monique.dubois@outlook.fr", "M0nique!Books", "33123456789")
address6 = ShippingAddress("14 Rue de Rivoli", "Paris", "FR", "75004", "France")
user6.set_shipping_address(address6)
user_list.add_user(user6)


#6 BOOKS added to have data to handle when the program starts
book_list = BookInventory("Book Collection")
book1 = (Book("DU1", "Dune", "Frank Herbert", 14.99, 8, BookGenre.SCIFI, "9780441172719", 1965, Language.ENGLISH, "Chilton Books",
         BookFormat.PAPERBACK) )
book2 = Book("TM01", "The Martian", "Andy Weir", 12.50, 4, BookGenre.SCIFI, "9780804139021", 2014, Language.ENGLISH, "Crown Publishing Group",
             BookFormat.HARDCOVER)
book3 = Book("GDT01", "The Girl with the Dragon Tattoo", "Stieg Larsson", 11.99, 5, BookGenre.MYSTERY, "9780307949486", 2005, Language.FRENCH, "Norstedts Förlag",
             BookFormat.HARDCOVER)
book4 = Book("GG01", "Gone Girl", "Gillian Flynn", 10.99, 8, BookGenre.MYSTERY, "9780307588371", 2012, Language.PORTUGUESE, "Crown Publishing Group",
             BookFormat.PAPERBACK)
book5 = Book("SJ01", "Steve Jobs", "Walter Isaacson", 18, 16, BookGenre.BIOGRAPHY, "9781451648539", 2011, Language.SPANISH, "Simon & Schuster",
             BookFormat.EBOOK)
book6 = Book("BE01", "Becoming", "Michelle Obama", 16.99, 12, BookGenre.BIOGRAPHY, "9781524763138", 2018, Language.ENGLISH, "Crown Publishing Group",
             BookFormat.HARDCOVER)

#Adding 6 books to a book list/collection
book_list.add_book(book1)
book_list.add_book(book2)
book_list.add_book(book3)
book_list.add_book(book4)
book_list.add_book(book5)
book_list.add_book(book6)

# 10 ORDERS added to have data to handle when the program starts
order_list = OrderInventory("Order Collection")

order99 = Order("0482110", user0, OrderStatus.PLACED)
order99.add_book_to_order(book1)
order99.add_book_to_order(book2)
order99.set_order_date("Wed 7 May 2025 13:12:23")
order99.set_order_status(OrderStatus.SHIPPED)
user0.add_order(order99)

order1 = Order("0482110", user1, OrderStatus.PLACED)
order1.add_book_to_order(book1)
order1.add_book_to_order(book2)
order1.set_order_date("Wed 7 May 2025 13:12:23")
order1.set_order_status(OrderStatus.DELIVERED)
user1.add_order(order1)

order2 = Order("0473112", user2, OrderStatus.PLACED)
order2.add_book_to_order(book2)
order2.add_book_to_order(book3)
order2.add_book_to_order(book4)
order2.set_order_date("Thu 8 May 2025 12:28:58")
order2.set_order_status(OrderStatus.DELIVERED)
user2.add_order(order2)

order3 = Order("0464118", user3, OrderStatus.PLACED)
order3.add_book_to_order(book1)
order3.add_book_to_order(book4)
order3.add_book_to_order(book5)
order3.set_order_date("Thu 9 May 2025 15:53:18")
order3.set_order_status(OrderStatus.DELIVERED)
user3.add_order(order3)

order4 = Order("0450108", user2, OrderStatus.PLACED)
order4.add_book_to_order(book6)
order4.set_order_date("Thu 9 May 2025 22:05:07")
order4.set_order_status(OrderStatus.DELIVERED)
user2.add_order(order4)

order5 = Order("0450106", user5, OrderStatus.DELIVERED)
order5.add_book_to_order(book4)
order5.set_order_date("Sat 10 May 2025 14:03:02")
order5.set_order_status(OrderStatus.DELIVERED)
user5.add_order(order5)

order6 = Order("0011122", user0, OrderStatus.DELIVERED)
order6.add_book_to_order(book3)
order6.set_order_date("Sat 10 May 2025 11:13:22")
order6.set_order_status(OrderStatus.DELIVERED)
user0.add_order(order6)

order7 = Order("0099932", user4, OrderStatus.DELIVERED)
order7.add_book_to_order(book1)
order7.set_order_date("Fri 9 May 2025 7:11:03")
order7.set_order_status(OrderStatus.DELIVERED)
user4.add_order(order7)

order8 = Order("0099930", user6, OrderStatus.DELIVERED)
order8.add_book_to_order(book3)
order8.add_book_to_order(book6)
order8.add_book_to_order(book2)
order8.set_order_date("Fri 9 May 2025 4:09:56")
order8.set_order_status(OrderStatus.DELIVERED)
user6.add_order(order8)

order9 = Order("0099931", user6, OrderStatus.DELIVERED)
order9.add_book_to_order(book5)
order9.add_book_to_order(book4)
order9.set_order_date("Wed 7 May 2025 16:07:13")
order9.set_order_status(OrderStatus.DELIVERED)
user6.add_order(order9)

#Adding 10 orders to the order list/collection
order_list.add_order(order99)
order_list.add_order(order1)
order_list.add_order(order2)
order_list.add_order(order3)
order_list.add_order(order4)
order_list.add_order(order5)
order_list.add_order(order6)
order_list.add_order(order7)
order_list.add_order(order8)
order_list.add_order(order9)



# ------------- Helper Functions  ------------- #
def add_book(current_order):
    """prints the list of current books, add 1 book at a time through its ID based on user input. Displays Total Qty & $"""
    print("Select a book from the list typing its ID:")
    available_books = book_list.get_book_list()
    book_list.display_short_book_list()

    choice = input().upper().strip()

    for book in available_books:
        if book.get_book_id() == choice:
            if book.get_quantity() != 0:
                current_order.add_book_to_order(book)
                book.set_quantity(book.get_quantity() - 1)
                print(f"✅ Added {book.get_title()} ({book.get_book_id()}) to your order.\n"
                      f"🛍️ Your Shopping cart:\n"
                      f"\tItems: {current_order.get_total_items()}\n"
                      f"\tTotal: ${current_order.get_total_amount()}")
                return
            else:
                print("🙏 We're sorry. We don't have more books available. Try with a different book or click here to join the wait list.")
                return
    else:
        print("❌ Invalid book ID. Please try again or contact the Administrator.")

def remove_book(current_order):
    """Subtract 1 book at a time through its ID (user input), Displays updated Qty & $"""
    print("Select the book you want to remove from your cart by typing its ID:")
    books_on_shopping_cart = current_order.get_book_list()

    choice = input().upper().strip()

    for book in books_on_shopping_cart:
        if book.get_book_id() == choice:
            current_order.remove_book_from_order(book)
            book.set_quantity(book.get_quantity() + 1)
            print(f"✅ Removed {book.get_title()} ({book.get_book_id()}) from your order.\n"
                  f"🛍️ Your Shopping cart:\n"
                  f"\tItems: {current_order.get_total_items()}\n"
                  f"\tTotal: ${current_order.get_total_amount()}")
            return
    print("❌ Invalid book ID. Please try again or contact the Administrator.")


def check_email(email):
    """Checks if email already exists. If true -> shows message & asks input again."""
    for e in user_list.get_email_list():
        if e.upper().strip() == email:
            return True
    return False

def check_username(username):
    """Checks if username already exists. If true -> shows message & asks input again."""
    for user in user_list.get_username_list():
        if user.upper().strip() == username.upper().strip():
            return True
    return False

def check_password(password):
    """Checks if password matches. If False -> shows message & asks input again."""
    for password_database in user_list.get_password_list():
        if password_database.upper().strip() == password.upper().strip():
            return True
    return False


def get_user_by_username(username):
    """Retrieves the user email by its username"""
    username = username.upper().strip()
    for user in user_list.get_user_list():
        if user.get_username().upper().strip() == username:
            return user
    return None

def get_shipping_address_by_username(username):
    """Retrieves the shipping address by its username"""
    username = username.upper().strip()
    for user in user_list.get_user_list():
        if user.get_username().upper().strip() == username:
            return user
    return None

def login_user_order_placement():
    """Checks if username & password exists. If yes, set username for current order & places the order. Then resets
    to an empty order to start all over again"""
    global order #To use & change the order variable inside this function

    while True:
        username = input("Username: ")
        try:
            if not check_username(username):
                raise ValueError
            break
        except ValueError:
            print(f"❌ Invalid Username. This username {username} is not registered. Please try again.")

    while True:
        password = input("Password: ")
        try:
            if not check_password(password):
                raise ValueError
            break
        except ValueError:
            print(f"❌ Invalid Password. Just for test purposes {password}. Please try again.")

            print("Username & password OK. You're logged in 🚀")


    # Check username & Retrieves the User object that matches this username
    user = get_user_by_username(username)

    # Set the User object for this order
    order.set_user(user)

    # Adds this order to the Order Collection (available from View Orders option)
    order_list.add_order(order)
    # Adds order to User's order list (purchase history)
    user.add_order(order)

    # Updates the Qty of the Book Collection (Book Collection qty - Order qty)
    book_list.subtract_order_book(order)
    # Sets order status as placed
    order.set_order_status(OrderStatus.PLACED)
    print(f"🥳 You have placed the order successfully.\n"
          f"Your Order:\n"
          f"{order}")
    #Restarts a new order
    new_timestamp = datetime.now()
    new_order_id = new_timestamp.strftime("0%M%S%H")
    #This will create a new Order object to restart with an empty order after placement
    order = Order(new_order_id, OrderStatus.NEW_ORDER)


def register_shipping_address(username):
    """Takes user inputs to register a new shipping & Creates a new Shipping Address Object & Assign it to User
    Object"""
    print("Enter details for your shipping address: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    postal_code = input("Postal Code: ")
    country = input("Country: ")

    #Wrapping up user inputs in a ShippingAddress object
    new_shipping_address = ShippingAddress(street, city, state, postal_code, country)

    #Checking username & assigning new_shipping_address to the User object with that username
    username = username.upper().strip()
    for user in user_list.get_user_list():
        if user.get_username().upper().strip() == username:
            user.set_shipping_address(new_shipping_address)

    print(f"✅ Shipping Address has been added to your account.\n"
          f"{new_shipping_address}")

def register_user():
    """Takes user inputs to register a new user & adds new User object to UserInventory object"""
    print("Enter the following details to create a user: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    while True:
        email = input("Email: ")
        try:
            if check_email(email):
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid Email. It is already taken. Please try again.")

    while True:
        username = input("Username: ")
        try:
            if check_username(username):
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid Username. It is already taken. Please try again.")

    password = input("Password: ")
    phone_number = input("Phone Number: ")
    new_user = User(first_name, last_name, username, email, password, phone_number)
    user_list.add_user(new_user)
    register_shipping_address(username)

    print(f"✅ User {username} has been created.")
    return new_user


def place_order():
    """Displays order summary & user confirmation to proceed with existing account or new account"""
    order.display_order_summary()
    #Confirm to place the order
    print("Enter Confirm to proceed with the checkout or Cancel to go back to the main menu.")
    while True:

        choice = input().upper().strip()

        if choice == "CONFIRM":
            ask_user_new_or_existing()
            break
        elif choice == "CANCEL":
            print("You have canceled the order placement. But your selected items are still there... just in case 😊")
            break
        else:
            print("❌ Invalid option. Please select a valid one.")



def ask_user_new_or_existing():
    """Asks user if he/she has an account or wants to create a new one to proceed with the order placement"""
    while True:
        print("Do you have an account? Select an option:")
        print("1. I have an account. I want to log-in\n"
              "2. I don't have an account. I want to create one.")
        choice = input().upper().strip()
        if choice == "1":
            login_user_order_placement()
            break
        elif choice == "2":
            register_user()
            break
        else:
            print("❌ Invalid option. Please select a valid one.")


def check_book_id(book_id):
    """Checks if Book ID exists, if Yes -> shows a message"""
    for book in book_list.get_book_id_list():
        if book.upper().strip() == book_id.upper().strip():
            return True
    return False

def set_book_genre(book):
    """Takes user inputs & retrieves a book genre based on user choice"""
    while True:
        print(f"📘 Available Book Formats:\n"
              f"Select an option from the list:\n"
              f"1. Fiction\n"
              f"2. Non-Fiction\n"
              f"3. Sci-Fi\n"
              f"4. Mistery\n"
              f"5. Biography\n"
              f"0. Cancel\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
            book.set_book_genre(BookGenre.FICTION)
            break
        elif user_choice == "2":
            book.set_book_genre(BookGenre.NONFICTION)
            break
        elif user_choice == "3":
            book.set_book_genre(BookGenre.SCIFI)
            break
        elif user_choice == "4":
            book.set_book_genre(BookGenre.MYSTERY)
            break
        elif user_choice == "5":
            book.set_book_genre(BookGenre.BIOGRAPHY)
            break
        elif user_choice == "0":
            print("A Book item cannot be entered without book genre.")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 5 to select an option.")


def set_book_language(book):
    """Takes user inputs & retrieve a language based on user choice"""
    while True:
        print(f"📘 Available Languages:\n"
              f"Select an option from the list:\n"
              f"1. English\n"
              f"2. Spanish\n"
              f"3. Portuguese\n"
              f"4. French\n"
              f"0. Cancel\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
            book.set_language(Language.ENGLISH)
            break
        elif user_choice == "2":
            book.set_language(Language.SPANISH)
            break
        elif user_choice == "3":
            book.set_language(Language.PORTUGUESE)
            break
        elif user_choice == "4":
            book.set_language(Language.FRENCH)
            break
        elif user_choice == "0":
            print("A Book item cannot be entered without language.")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 4 to select an option.")


def set_book_format(book):
    """Takes user inputs & retrieves a book format based on user choice"""
    while True:
        print(f"📘 Available Book Formats:\n"
              f"Select an option from the list:\n"
              f"1. Hardcover\n"
              f"2. Paperback\n"
              f"3. eBook\n"
              f"4. Audiobook\n"
              f"0. Cancel\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
            book.set_book_format(BookFormat.HARDCOVER)
            break
        elif user_choice == "2":
            book.set_book_format(BookFormat.PAPERBACK)
            break
        elif user_choice == "3":
            book.set_book_format(BookFormat.EBOOK)
            break
        elif user_choice == "4":
            book.set_book_format(BookFormat.AUDIOBOOK)
            break
        elif user_choice == "0":
            print("A Book item cannot be entered without book format.")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 4 to select an option.")

def get_valid_float(user_value):
    while True:
        try:
            user_input = input(user_value)
            value = float(user_input) #It checks if it is a float number, if not -> shows error
            return value
        except ValueError:
            print(f"❌ Invalid value. Try again using only numbers with decimals or positive ones.")

def get_valid_integer(user_value):
    while True:
        try:
            user_input = input(user_value)
            value = int(user_input)
            return value
        except ValueError:
            print(f"❌ Invalid value. Try again using only integers (no decimals, no negative numbers).")


def register_book():
    """Takes user inputs to register a new book & adds new Book object to BookInventory object"""
    new_book = Book(None, None, None, None, None, None, None, None,None ,None, None)
    print("Enter the following details to register a new book: ")
    while True:
        book_id = input("Book ID 'e.g. Initials & number': ")
        try:
            if check_book_id(book_id):
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid Book ID. It is already taken. Please try again.")

    title = input("Title: ")
    author = input("Author: ")

    price = get_valid_float("Price: ")
    quantity = get_valid_integer("Quantity: ")

    set_book_genre(new_book)
    if new_book.get_book_genre() is None:
        print("Book registration canceled.")
        return
    genre = new_book.get_book_genre()

    isbn = get_valid_integer("ISBN (Type only numbers): ")

    publisher = input("Publisher: ")

    publication_year = get_valid_integer("Publication Year: ")

    set_book_language(new_book)
    if new_book.get_language() is None:
        print("Book registration canceled.")
        return
    book_language = new_book.get_language()

    set_book_format(new_book)
    if new_book.get_book_format() is None:
        print("Book registration canceled.")
        return
    book_format = new_book.get_book_format()

    #formatting before wrap it up as Book object
    book_id = book_id.upper()
    title = title.title()
    author = author.title()
    publisher = publisher.title()

    new_book = Book(book_id, title, author, price, quantity, genre, isbn, publication_year, book_language, publisher, book_format)
    book_list.add_book(new_book)
    print(f"✅ Book {new_book.get_book_id()} {new_book.get_title()} with {new_book.get_quantity()} units has been created.")
    return new_book


def view_order_by_id():
    """Checks an order by its order ID & retrieves the order details"""
    while True:
        print("Enter your order ID or Cancel: ")
        # Checking username & assigning new_shipping_address to the User object with that username
        choice = input().upper().strip()

        if choice == "CANCEL":
            main_menu()
            return

        for item in order_list.get_order_list():
            if item.get_order_id().upper().strip() == choice:
                print(item)
                return

        print("❌ Invalid option. Please select a valid one.")

def display_books():
    """prints the list of Book objects: total number of books & display book details"""
    print(book_list)
    book_list.display_book_list()

def display_users():
    """prints the list of User objects: total number of users & display user details"""
    print(user_list)
    user_list.display_user_list()

def display_orders():
    """prints the list of Order objects: total number of orders, total amount of sells & display order details"""
    print(order_list)
    order_list.display_order_list()

def main_menu():
    """Runs the main menu to display the options to the users"""
    while True:
        print(f"🛍️ Orders:\n"
              f"1. Add Book\n"
              f"2. Remove Book\n"
              f"3. Place Order\n"
              f"4. Check Order Status\n"
              f"5. View Orders\n\n"
              f"📚 Books:\n"
              f"6. Register New Book\n"
              f"7. View Books\n\n"
              f"🙋‍♀️ Users:\n"
              f"8. Register New User\n"
              f"9. View Users\n"
              f"0. Exit Program\n")
        user_choice = input("Select an option: ").strip()
        if user_choice == "1":
            add_book(order)
        elif user_choice == "2":
            if order.get_total_items() != 0:
                remove_book(order)
            else:
                print("You have 0 items in your cart. Nothing to remove from.")
        elif user_choice == "3":
            if order.get_total_items() != 0:
                place_order()
            else:
                print("You have 0 items in your cart. No order to place. Try adding some items first.")
        elif user_choice == "4":
            view_order_by_id()
        elif user_choice == "5":
            display_orders()
        elif user_choice == "6":
            register_book()
        elif user_choice == "7":
            display_books()
        elif user_choice == "8":
            register_user()
        elif user_choice == "9":
            display_users()
        elif user_choice == "0":
            print("You have exited Bookiverse. See you next time!")
            break
        else:
            print("❌ Invalid option. Try again using from 0 to 9 to select an option.")

def welcome():
    """To welcome the user when starting the program. As eCommerce, no login is required to browse site."""
    print("-" * 40)
    print("🌎📚 Welcome to Bookiverse 📚🌎\n"
          "Explore our selection of Best Sellers, eBooks, Audiobooks and much more.\n"
          "What would you like to do next? Select an option:\n")

# ------------- START Main Program  ------------- #

timestamp = datetime.now()
order_id = timestamp.strftime("0%M%S%H")
order = Order(order_id, OrderStatus.NEW_ORDER)
#Assumption made: User has permission to see other people's orders.
# e.g. A staff member of the Bookiverse store that can also register and buy as a new different user."
welcome()
main_menu()

# ------------- END Main Program  ------------- #

## End of the script - 1847863 F. Scolari KBS May 2025 TECH6100 Assessment 2