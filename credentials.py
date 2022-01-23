import string
import random


class Credentials:
    user_passwords = []

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username
        self.password = password


    def save_platform_credentials(self):
        """method that appends credentials to the user passwords array"""
        Credentials.user_passwords.append(self)

    def delete_platform_credentials(self):
        """removes credentials from the user passwords array"""
        Credentials.user_passwords.remove(self)

    @classmethod
    def platform_exists(cls, platform):
        """method to check if a platform exists"""
        for platform_credentials in cls.user_passwords:
            return True if platform_credentials.platform == platform else False

    @classmethod
    def find_platform_credentials(cls, platform):
        """method to find platform credentials by platform name"""
        for platform_credentials in cls.user_passwords:
            if platform_credentials.platform == platform:
                return platform_credentials

    @classmethod
    def display_all_credentials(cls):
        """method to display all saved credentials"""
        return cls.user_passwords

    @staticmethod
    def gernerate_password(password_length=6):
        """method to generate a random password"""
        random_string = string.ascii_letters + string.digits
        random_string = random.sample(random_string, password_length)
        return "".join(random_string)

    def __repr__(self):
        """format credential print"""
        return f"Platform: {self.platform} Username: {self.username} Password: {self.password}"

