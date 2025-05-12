# TECH6100 Assessment 2 Florencia Scolari ID 1847863 May 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100-A2.git
#todo: check & complete out-of-scope features
from datetime import datetime

# User for Testing Purposes:
# First Name: Elle
# Last Name: Test
# Username: test2025
# Email: test@t.com.au
# Password: 123
# Order ID: 0011122

# Out of scope:
# 1. Global command to cancel an ongoing task.
# 2. Validation of data type for user inputs when registering a new user. e.g. They can put letters as a phone number.
# 3. Turning back for case: If user selects she/he has an account and doesn't know username & password, no way to recover from that. Dead End.
# 4. Login as different user types at tge beginning. You can create account & login to place an order.

# PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

#from enum import StrEnum

from Book import Book, BookGenre, BookFormat, Language, BookInventory
from Order import OrderStatus, Order, OrderInventory
#from Order import OrderStatus, Order
from User import User, ShippingAddress, UserInventory

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
                print("We're sorry. We don't have more books available. Try with a different book or click here to join the wait list.")
                return
    else:
        print("Invalid book ID. Please try again or contact the Administrator.")

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
    print("Invalid book ID. Please try again or contact the Administrator.")


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
    """Checks if username & password exists. If yes, set username for current order & places the order."""
    while True:
        username = input("Username: ")
        try:
            if not check_username(username):
                raise ValueError
            break
        except ValueError:
            print(f'Invalid Username. This username {username} is not registered. Please try again.')

    while True:
        password = input("Password: ")
        try:
            if not check_password(password):
                raise ValueError
            break
        except ValueError:
            print(f'Invalid Password. Just for test purposes {password}. Please try again.')

            print("username & password OK. You're logged in!")


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
            print('Invalid Email. It is already taken. Please try again.')

    while True:
        username = input("Username: ")
        try:
            if check_username(username):
                raise ValueError
            break
        except ValueError:
            print('Invalid Username. It is already taken. Please try again.')

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
            print("You have cancel the order placement. Your selected items are still there :) ")
            break
        else:
            print("Invalid option. Please select a valid one.")



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
            print("Invalid option. Please select a valid one.")


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
            print("Invalid option. Try again using from 0 to 5 to select an option.")


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
            print("Invalid option. Try again using from 0 to 4 to select an option.")


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
            print("Invalid option. Try again using from 0 to 4 to select an option.")

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
            print('Invalid Book ID. It is already taken. Please try again.')

    title = input("Title: ")
    author = input("Author: ")
    #todo: validate that enters number
    price = float(input("Price: "))
    # todo: validate that enters number
    quantity = int(input("Quantity: "))

    set_book_genre(new_book)
    if new_book.get_book_genre() is None:
        print("Book registration canceled.")
        return
    genre = new_book.get_book_genre()

    isbn = input("ISBN: ")
    publisher = input("Publisher: ")
    # todo: validate that enters number
    publication_year = int(input("Publication Year: "))

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
    price = price.__float__()

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

        print("Invalid option. Please select a valid one.")

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
            print("You have exited the program. Until next time.")
            break
        else:
            print("Invalid option. Try again using from 0 to 9 to select an option.")

# ------------- Main Program  ------------- #


timestamp = datetime.now()
order_id = timestamp.strftime("0%M%S%H")
order = Order(order_id, OrderStatus.NEW_ORDER)

main_menu()
