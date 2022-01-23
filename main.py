#!/usr/bin/env python3.6
from user import User
from credentials import Credetials


def create_user(first_name, last_name, username, password):
    return User(first_name, last_name, username, password)


def show_options():
    print("Please choose an option to continue: ")
    print("1. Create Account\n2. Login\n3. Display Accounts\n4. Exit")


def create_account_option():
    print("Please provide the following details to create an account")
    print('*' * 70)

    print("Enter your first name .....")
    first_name = input()
    print("Enter your last name .....")
    last_name = input()
    print("Enter your username .....")
    username = input()
    print("Enter password .....")
    user_password = input()

    user = create_user(first_name, last_name, username, user_password)

    user.save_user()

    return user

def user_login():
    print("Enter your details to login")
    print("Enter your username .....")
    username = input()
    print("Enter password .....")
    user_password = input()

    return User.login(username, user_password)


def show_password_options():
    print("Please choose an option to set the password")
    print("1. Enter your password\n2. Generate a password")

    choice = int(input())

    if choice == 1:
        print("Enter platform password")
        password = input()

    else:
        length = int(input("Please provide the length of the password to be generated\n"))
        password = Credetials.gernerate_password(length)
        print(f"The generated password is: {password}")

    return password

def display_logged_in_menu():
    print("Please select an option")
    print("1. Save new credentials\n2. Show all saved credentials\n3. Delete credentials\n4. Logout")
    choice = int(input())
    # while True:
    if choice == 1:
        print("-"*20 + "Save Platform Credentials" + "-"*20)
        print("Enter platform name eg github, facebook")
        platform = input()

        print("Enter platform username eg john")
        username = input()

        password = show_password_options()

        creds = Credetials(platform, username, password)
        creds.save_platform_credentials()

        print(f"\n\nCredentials for {platform} saved successfully\n\n")

    elif choice == 2:
        print("-" * 20 + "Show all saved credentials" + "-"*20)
        print(Credetials.display_all_credentials())

    elif choice == 3:
        print("-" * 20 + "Delete platform credentials" + "-"*20)
        print("Enter the name of the platform you want to delete")

        delete_patform = input()

        if Credetials.platform_exists(delete_patform):
            plat = Credetials.find_platform_credentials(delete_patform)
            plat.delete_platform_credentials()
            print(f"platform {delete_patform} deleted successfully\n\n")
        else:
            print(f"platform {delete_patform} does not exist!")

    elif choice == 4:
        print("Logging out" + "." * 20)
        return True


def main():
    print("*"*40 + " WELCOME TO PASSWORD LOCK " + "*"*40)
    show_options()

    while True:
        try:
            choice = int(input())

            if choice is 1:
                user = create_account_option()
                print(f"Welcome to Password Locker {user.username}")
                while True:
                    logout = display_logged_in_menu()
                    if logout:
                        show_options()
                        break

            elif choice == 2:
                if user_login():
                    print(f"Welcome to Password Locker")
                    while True:
                        logout = display_logged_in_menu()
                        if logout:
                            show_options()
                            break
                else:
                    print("Account does not exist")
                    show_options()

            elif choice == 3:
                print("Registered user accounts")
                print(User.display_user_accounts())
                show_options()


            elif choice == 4:
                break
            else:
                raise Exception()
        except:
            print("You selected an invalid option")
            show_options()

if __name__ == '__main__':
    main()

