#User login
def login_user(username):
    print(f'{username} successfully logged in!!')
def check_password(password):
    if password == '1234':
        return True
    else:
        return False

def check_email(email):
    if email == '1234':
        return True
    else:
        return False
username = input('Enter username')
password = input('Enter password')
email = input('Enter email')
try:
    if not check_email(email):
        raise ValueError
except ValueError:
    print('Wrong Password! Try again!')
else:
     login_user(username)


order99 = Order("0482110", user0, OrderStatus.PLACED)
order99.add_book_to_order(book1)
order99.add_book_to_order(book2)
order99.set_order_date("Wed 7 May 2025 13:12:23")
order99.set_order_status(OrderStatus.SHIPPED)

order1 = Order("0482110", user1, OrderStatus.PLACED)
order1.add_book_to_order(book1)
order1.add_book_to_order(book2)
order1.set_order_date("Wed 7 May 2025 13:12:23")
order1.set_order_status(OrderStatus.DELIVERED)

order2 = Order("0473112", user2, OrderStatus.PLACED)
order2.add_book_to_order(book2)
order2.add_book_to_order(book3)
order2.add_book_to_order(book4)
order2.set_order_date("Thu 8 May 2025 12:28:58")
order2.set_order_status(OrderStatus.DELIVERED)

order3 = Order("0464118", user3, OrderStatus.PLACED)
order3.add_book_to_order(book1)
order3.add_book_to_order(book4)
order3.add_book_to_order(book5)
order3.set_order_date("Thu 9 May 2025 15:53:18")
order3.set_order_status(OrderStatus.DELIVERED)

order4 = Order("0450108", user2, OrderStatus.PLACED)
order4.add_book_to_order(book6)
order4.set_order_date("Thu 9 May 2025 22:05:07")
order4.set_order_status(OrderStatus.DELIVERED)

order5 = Order("0450106", user5, OrderStatus.DELIVERED)
order5.add_book_to_order(book4)
order5.set_order_date("Sat 10 May 2025 14:03:02")
order5.set_order_status(OrderStatus.DELIVERED)

order6 = Order("0011122", user0, OrderStatus.DELIVERED)
order6.add_book_to_order(book3)
order6.set_order_date("Sat 10 May 2025 11:13:22")
order6.set_order_status(OrderStatus.DELIVERED)