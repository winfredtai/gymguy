from qbay.models import Product, login, register, \
    update_product, update_user, create_product


def login_page():
    email = input('Please input email:')
    password = input('Please input password:')
    return login(email, password)


def profile_update_page():
    email = input('Please input email:')
    username = input('Please input username:')
    shipping_address = input('Please input shipping_address:')
    postal_code = input('Please input postal_code:')
    return update_user(email, username, shipping_address, postal_code)


def login_success_page():
    while True:
        selection1 = input(
            'Welcome. Your options are as follows\n'
            '1. Update your profile\n'
            '2. Go to the home page\n'
            '3. Log out\n'
            'Please enter the number corresponding to what '
            'you would like to do.\n')
        selection1 = selection1.strip()
        if selection1 == '1':
            NewP = profile_update_page()
            if NewP:
                print("profile update succeed")
            else:
                print('profile update failed')
        elif selection1 == '2':
            home_page()
        elif selection1 == '3':
            break
        else:
            print("Invalid Input")


def register_page():
    user_name = input('Please input user name:')
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register(user_name, email, password):
        print('registration succeeded')
    else:
        print('registration failed.')


def create_product_page():
    Title = input('Please input product title:')
    Description = input('Please input product description:')
    Price = float(input('Please input product price:'))
    Owner_email = input('Please input product owner email:')
    if create_product(Title, Description, Price, Owner_email):
        print('Create product success')
    else:
        print('product create failed????.')


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
        print('Update product succeeded')
    else:
        print('Update product failed.')


def home_page():
    while True:
        selection = input(
            'Welcome to the home page. Your options are as follows:\n'
            '1: Update Product Page\n'
            '2: Create Product Page\n'
            '3: Return to Main Screen\n'
            'Please enter the number corresponding to what you '
            'would like to do.\n')
        selection = selection.strip()
        if selection == 1:
            product2 = update_product_page()
            if product2:
                print('Update product succeeded.')
                break
            else:
                print('Update product failed.')
        elif selection == 2:
            create_product_page()
        elif selection == 3:
            break
        else:
            print('Invalid input, please try again.')
