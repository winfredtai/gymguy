from qbay import *
from qbay.cli import login_page, register_page, login_success_page


def main():
    while True:
        selection = input(
            'Welcome. Your options are as follows\n'
            '1: User Login\n'
            '2: User Registration\n'
            '3: Exit the system\n'
            'Please enter the number corresponding to what '
            'you would like to do.\n')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                login_success_page()
            else:
                print('login failed')
        elif selection == '2':
            register_page()
        elif selection == '3':
            print("See you next time")
            exit(0)
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
