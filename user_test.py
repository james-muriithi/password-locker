import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("james", "muriithi", "james-muriithi", "password")


    def test_user_created(self):
        self.assertEqual(self.user.first_name, "james")
        self.assertEqual(self.user.last_name, "muriithi")
        self.assertEqual(self.user.username, "james-muriithi")
        self.assertEqual(self.user.password, "password")

    def test_user_saved(self):
        self.assertEqual(len(User.display_user_accounts()), 0)
        self.user.save_user()
        self.assertEqual(len(User.display_user_accounts()), 1)

