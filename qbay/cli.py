from qbay.models import Product, login, register, update_product


def login_page():
    email = input('Please input email:')
    password = input('Please input password:')
    return login(email, password)


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


def regsiter_page():
    user_name = input('Please input user name:')
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register(user_name, email, password):
        print('registration succceeded')
    else:
        print('regisration failed.')


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
