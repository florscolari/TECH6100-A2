# TECH6100 Assessment 2 Florencia Scolari ID 1847863 May 2025
# Check the full project and references on the GitHub Public Repo https://github.com/florscolari/TECH6100-A2.git
#todo: check & complete out-of-scope features

# Out of scope: global command to cancel an ongoing task.

#PEP 8 Naming Conventions:
# Variable name: lowercase_with_underscores - user_name
# Function name: verb_lowercase_underscore - send_email()
# Class name: CapitaliseWords - UseNouns

#from enum import StrEnum

from Book import Book, BookGenre, BookFormat, Language, BookInventory
#from Order import OrderStatus, Order
from User import User, ShippingAddress, UserInventory

#6 BOOKS added to have data to handle when the program starts
book_list = BookInventory("Book Collection")
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

#Adding 6 books to a book list/collection
book_list.add_book(book1)
book_list.add_book(book2)
book_list.add_book(book3)
book_list.add_book(book4)
book_list.add_book(book5)
book_list.add_book(book6)

#6 USERS added to have data to handle when the program starts (3 of 6 with Address)
user_list = UserInventory("User Collection")
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
user_list.add_user(user4)

user5 = User("Michael", "Singh", "read4growth", "michael.singh.reads@example.in", "M1chael#Grow", "912240011122")
user_list.add_user(user5)

user6 = User("Monique", "Dubois", "momo_reads", "monique.dubois@outlook.fr", "M0nique!Books", "33123456789")
user_list.add_user(user6)






# ------------- Helper Functions  ------------- #
def add_book():
    pass

def register_user():
    pass

def place_order():
    pass

def display_books():
    """prints the list of Book objects: total number of books & display book details"""
    print(book_list)
    book_list.display_book_list()

def display_users():
    """prints the list of User objects: total number of users & display user details"""
    print(user_list)
    user_list.display_user_list()

def display_orders():
    pass

def main_menu():
    while True:
        print(f"1. Add Book\n"
              f"2. Register User\n"
              f"3. Place Order\n"
              f"4. View Books\n"
              f"5. View Users\n"
              f"6. View Orders\n"
              f"0. Exit Program")
        user_choice = input("Select an option: ")
        if user_choice == "1":
            add_book()
        elif user_choice == "2":
            register_user()
        elif user_choice == "3":
            place_order()
        elif user_choice == "4":
            display_books()
        elif user_choice == "5":
            display_users()
        elif user_choice == "6":
            display_orders()
        elif user_choice == "0":
            print("You have exited the program. Until next time.")
            break
        else:
            print("Invalid option. Try again using from 0 to 6 to select an option.")

# ------------- Main Program  ------------- #


order_inventory = []

main_menu()
