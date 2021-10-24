from qbay.models import Product, login, register, update_product


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


def update_product_page():
    old_title = input('Please input product old title\
                      for finding specific product:\n')
    title = input('Please input new title:\n')
    description = input('Please input product description:\n')
    price = float(input('Please input new price'))
    product = Product.query.fileter_by(title=old_title).first()
    if product.product_id is None:
        print('Cannot find product')
    elif title is None:
        print('New title cannot be empty')
    elif description is None:
        print('Product description cannot be empty.')
    elif price < product.price:
        print('Price can only be increased.')
    elif update_product(old_title=old_title,
                        newTitle=title,
                        newDescription=description,
                        newPrice=price):
        print('Update product secceeded')
    else:
        print('Update product failed.')


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
