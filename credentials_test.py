import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        """setup method that runs before each test case"""
        self.platform = Credentials("github", "james-muriithi", "123456")
        Credentials.user_passwords = []

    def test_platform_created(self):
        """Method that tests if the constructor works"""
        self.assertEqual(self.platform.platform, "github")
        self.assertEqual(self.platform.username, "james-muriithi")
        self.assertEqual(self.platform.password, "123456")

    def test_save_platform_credentials(self):
        """tests credentials save method if it appends to array"""
        self.assertEqual(len(Credentials.user_passwords), 0)
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 1)

    def test_delete_platform_credentials(self):
        """tests if the delete credentials method removes from the array"""
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 1)
        self.platform.delete_platform_credentials()
        self.assertEqual(len(Credentials.user_passwords), 0)

    def test_platform_exists(self):
        """test if the platform_exists method returns the correct value"""
        self.platform.save_platform_credentials()
        self.assertEqual(Credentials.platform_exists(self.platform.platform), True)

    def test_find_platform_credentials(self):
        """test if method returns the credentials if platform was provided"""
        self.platform.save_platform_credentials()
        self.assertEqual(Credentials.find_platform_credentials(self.platform.platform), self.platform)

    def test_display_all_credentials(self):
        """test display credentials method if it returns all the saved credentials"""
        self.platform.save_platform_credentials()

        self.assertEqual(Credentials.display_all_credentials(), Credentials.user_passwords)

    def test_gernerate_password(self):
        """test if the generated password length is the one specified"""
        self.assertEqual(len(Credentials.gernerate_password(8)), 8)


if __name__ == "__main__":
    unittest.main()

