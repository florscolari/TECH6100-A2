from datetime import datetime
from enum import StrEnum

import Book


class OrderStatus(StrEnum):
    """Creating set of immutable values for order statuses"""
    NEW_ORDER = "New Order"
    PLACED = "Placed"
    CONFIRMED = "Confirmed"
    DISPATCHED = "Dispatched"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"

#todo: Research how to get a datetime stamp
#todo: search how to get the shipping address based on the user email
class Order:

    def __init__(self, order_id, order_status=OrderStatus.NEW_ORDER, user_email=None):
        timestamp = datetime.now()
        self.__order_id = order_id
        self.__order_date = timestamp
        self.__order_status : OrderStatus = order_status
        self.__book_list = [] #list of objects as attribute of this object // books selected by the user
        self.__total_items = 0 #it'll be calculated
        self.__total_amount = 0 #it'll be calculated
        self.__user_email = user_email
        self.__shipping_address = None

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
        return self.__total_items

    def get_total_amount(self):
        price_list = []
        for book in self.__book_list:
            ind_price = book.get_price()
            price_list.append(ind_price)
        total_amount = sum(price_list)
        total_amount = round(total_amount, 2)
        return total_amount


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


class OrderInventory:
    def __init__(self, name):
        self.__name = name
        self.__order_list = []
        self.__total_orders = 0
        self.__total_sells = 0
        self.__total_items_sold = 0

    def __str__(self):
        return f"{self.__name}\nTotal Qty Orders: {self.__total_orders}\nTotal Books sold: {self.__total_items_sold}\nTotal Sold $: {round(self.__total_sells, 2)}"

    def display_order_list(self):
        for order in self.__order_list:
            print(f"{order.__str__()}")

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