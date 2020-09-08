class Credential:

    credentials_list = []

    def __init__(self, name, user_name, email, password):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_credentials(self):
        """
        save_credentials method that allows us to save new credentials
        """
        Credential.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes a specific credential from the credentials_list
        """
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        method takes an user_name and return credentials the matches the user_name

        Arg:
            user_name: user_name to search for
        Return:
            Credentials of person that matches the user_name.
        '''

        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                return credential

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credentials_list
        """
        return cls.credentials_list

    # def read_csv(self):
    #     with open('credentials.csv', 'r+') as csv_list:
    #         dict_reader = DictReader(csv_list)
    #         list_of_dictionaries = list(dict_reader)
    #         return list_of_dictionaries

    # def validate_username(self):
    #     user_name = input('Please enter your username: ')
    #     password = input('Enter password: ')

    #     list_of_dict = read_csv()
    #     my_details = {'a': 1, 'b': 2}
