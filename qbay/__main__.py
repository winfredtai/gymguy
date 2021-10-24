from qbay import *
from qbay.cli import login_page, register_page, home_page


def main():
    while True:
        selection = input(
            'Welcome. Your options are as follows\n'
            '1: User Login\n'
            '2: User Registration\n'
            '3: Home Page\n'
            'Please enter the number corresponding to what '
            'you would like to do.\n')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('login failed')
        elif selection == '2':
            regsiter_page()
        elif selection == '4':
            home_page()


if __name__ == '__main__':
    main()
