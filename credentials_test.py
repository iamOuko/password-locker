import unittest
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_credential = Credential(
            "Ezra", "ezzy96", "ezzy@ms.com", "1234")

    def tearDown(self):
        """
        Tear down method to run before each teat case
        """
        Credential.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.name, "Ezra")
        self.assertEqual(self.new_credential.user_name, "ezzy96")
        self.assertEqual(self.new_credential.email, "ezzy@ms.com")
        self.assertEqual(self.new_credential.password, "1234")

    def test_save_credential(self):
        '''
        Test if credential object is saved in credential_list
        '''
        self.new_credential.save_credentials()  # Saving new credential
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credential(self):
        '''
        Check if we can save multiple credential into the credential_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Test", "user", "test@user.com", "5678")
        test_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

    def test_delete_credentials(self):
        """
        test_delete_credential test case to check if a user can delete credentials
        """
        self.new_credential.save_credentials()
        test_credentials = Credential("Test", "user", "test@user.com", "5678")
        test_credentials.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_find_credentials_by_user_name(self):
        '''
        test to check if we can find a credentials by user_name and display information
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Ezra", "ezzy96", "ezzy@ms.com", "1234")
        test_credential.save_credentials()

        found_credential = Credential.find_by_user_name("ezzy96")
        self.assertEqual(found_credential.user_name, test_credential.user_name)

    def test_display_all_credentials(self):

        self.assertEqual(Credential.display_credentials(),
                         Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()
