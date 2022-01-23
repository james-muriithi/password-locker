import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """setup method that runs before each test case"""
        self.user = User("james", "muriithi", "james-muriithi", "password")
        User.user_accounts = []

    def test_user_created(self):
        """Method that tests if the constructor works"""
        self.assertEqual(self.user.first_name, "james")
        self.assertEqual(self.user.last_name, "muriithi")
        self.assertEqual(self.user.username, "james-muriithi")
        self.assertEqual(self.user.password, "password")

    def test_user_saved(self):
        """Test if user save method appends to array"""
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)

    def test_user_delete(self):
        """tests if delete user method removes user from array"""
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)
        self.user.delete_user()
        self.assertEqual(len(User.display_user_accounts()), 0)

    def test_login(self):
        """test if login method works if credentials are correct"""
        self.user.save_user()
        self.assertEqual(User.login(
            self.user.username, self.user.password), True)

    def test_find_user(self):
        """test if user can be searched with username"""
        self.user.save_user()
        self.assertEqual(User.find_user(self.user.username), self.user)

    def test_display_user_accounts(self):
        """test if show all accounts method shows all accounts in array"""
        self.user.save_user()
        self.assertEqual(User.display_user_accounts(), User.user_accounts)


if __name__ == "__main__":
    unittest.main()
