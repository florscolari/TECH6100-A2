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

#todo: display only __repr__ method for each class

    #To display data from a class object to users
    def __str__(self):
        order_list_str = "\n".join([f"- ID: {order.get_order_id()}\tItems: {order.get_total_items()}\tAmount: $"
                                    f"{order.get_total_amount()}\tDate:"
                                    f" {order.get_order_date()}"
                                    for order in self.__order_history])
        return (f"------\n"
                f"Name: {self.__first_name} {self.__last_name}\n"
                f"Username: {self.__username}\n"
                f"Email: {self.__email}\n"
                f"Phone Number: {self.__phone_number}\n" #todo: placeholders to display pretty phone: +44-20-7946-0636?
                f"Shipping Address: {self.__shipping_address}\n"
                f"Purchase History: {len(self.__order_history)} orders\n"
                f"{order_list_str}" #todo: count previous purchases & show details?
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
                f"Purchase History: {self.__order_history} : {type(self.__order_history)}" #todo: count
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

    def add_order(self, order):
        self.__order_history.append(order)


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
        return f"{self.__street} {self.__city} {self.__state} ({self.__zip_code}) {self.__country}"


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
        return f"{self.__name}\nCurrent users: {self.__total_users}\n"

    def display_user_list(self):
        for user in self.__user_list:
            print(f"{user.__str__()}")

    def add_user(self, user: User):
        self.__user_list.append(user)
        self.__total_users += 1

    def remove_user(self, user: User):
        self.__user_list.remove(user)
        self.__total_users -= 1