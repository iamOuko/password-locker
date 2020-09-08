class User:

    user_list = []

    def __init__(self, name, user_name, email, password):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_contact method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
