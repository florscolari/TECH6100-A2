from datetime import datetime
from enum import StrEnum

import Book
from User import User


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
    def add_book_to_order(self, book: Book):
        self.__book_list.append(book)
        self.__total_items = len(self.__book_list)
        self.__total_amount += book.get_price()

    def remove_book_from_order(self, book: Book):
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