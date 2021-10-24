from qbay.models import login, register


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def register_page():
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register('default name', email, password):
        print('registration succeeded')
    else:
        print('registration failed.')


def home_page():
    selection = input(
        'Welcome to the home page. Your options are as follows:\n'
        '1: Create Product Page\n'
        '2: Update Product Page\n'
        '3: Return to Main Screen\n'
        'Please enter the number corresponding to what you '
        'would like to do.\n')
    selection = selection.strip()
    if selection == 1:
        create_product_page()
    elif selection == 2:
        update_product_page()
    elif selection == 3:
        main()
