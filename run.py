from user import User
from credential import Credential


def create_user(name, user_name, email, password):
    """
    Function to create a new user
    """
    new_user = User(name, user_name, email, password)
    return new_user


def save_user(user):
    """
    Function that saves user
    """
    user.save_user()


def create_credential(name, user_name, email, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(name, user_name, email, password)
    return new_credential


def save_credential(credential):
    """
    Function that saves credential
    """
    credential.save_credentials()


def delete_credential(credential):
    '''
    Function that deletes credential
    '''
    credential.delete_credential()


def find_credential(user_name):
    '''
    Function that finds credential by user_name
    '''
    return Credential.find_by_user_name(user_name)


def main():
    print("Hello Welcome to you Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new account, dc - display credentials, fc -find a user_name, ex -exit ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print("Name: ")
            name = input()

            print("user_name: ")
            user_name = input()

            print("Email: ")
            email = input()

            print("Password: ")
            password = input()

            save_credential(create_credential(
                name, user_name, email, password))
            print('\n')
            print(f"New C {user_name}  created")
            print('\n')

        elif short_code == 'dc':

            if display_credential():
                print("Here is a list of all your credentials")
                print('\n')

                for credential in display_credential():
                    print(
                        f"{credential.name} {credential.user_name} {credential.email} {credential.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the user_name you want to search for")

            find_by_user_name = input()
            if find_by_user_name(user_name):
                user_name = find_by_user_name(user_name)
                print(f"{user_name.name} {user_name.email}")
                print("\n")

            else:
                print("That user_name does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("Wrong username")
