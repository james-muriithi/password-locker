import string
import random

class Credetials:
    user_passwords = []

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password


    def save_platform_credentials(self):
        Credetials.user_passwords.append(self)

    def delete_platform_credentials(self):
        Credetials.user_passwords.remove(self)

    @classmethod
    def find_platform_credentials(cls, platform):
        for platform_credentials in cls.user_passwords:
            return platform_credentials if platform_credentials.platform == platform else False

    @classmethod
    def display_all_credentials(cls):
        return cls.user_passwords

    @staticmethod
    def gerneratePassword(password_length=6):
        random_string = string.ascii_letters + string.digits
        random_string = random.sample(random_string, password_length)
        return "".join(random_string)

