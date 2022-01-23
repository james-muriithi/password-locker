import unittest
from credentials import Credetials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.platform = Credetials("github", "james-muriithi", "123456")
        Credetials.user_passwords = []

    def test_platform_created(self):
        self.assertEqual(self.platform.platform, "github")
        self.assertEqual(self.platform.username, "james-muriithi")
        self.assertEqual(self.platform.password, "123456")

    def test_save_platform_credentials(self):
        self.assertEqual(len(Credetials.user_passwords), 0)
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credetials.user_passwords), 1)

    def test_delete_platform_credentials(self):
        self.platform.save_platform_credentials()
        self.assertEqual(len(Credetials.user_passwords), 1)
        self.platform.delete_platform_credentials()
        self.assertEqual(len(Credetials.user_passwords), 0)

    def test_platform_exists(self):
        self.platform.save_platform_credentials()
        self.assertEqual(Credetials.platform_exists(self.platform.platform), True)

    def test_find_platform_credentials(self):
        self.platform.save_platform_credentials()
        self.assertEqual(Credetials.find_platform_credentials(self.platform.platform), self.platform)

    def test_display_all_credentials(self):
        self.platform.save_platform_credentials()

        self.assertEqual(Credetials.display_all_credentials(), Credetials.user_passwords)

    def test_gernerate_password(self):
        self.assertEqual(len(Credetials.gernerate_password(8)), 8)

