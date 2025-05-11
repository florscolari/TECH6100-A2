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