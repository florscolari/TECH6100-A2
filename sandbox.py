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
