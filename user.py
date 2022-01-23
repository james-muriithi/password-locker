class User:

    def __init__(self, first_name, last_name, username, password):
        """user constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    user_accounts = []

    def delete_user(self):
        """function to delete user account"""
        User.user_accounts.remove(self)

    @classmethod
    def login(cls, username, password):
        """Verify user credentials"""
        for user in cls.user_accounts:
            if user.username == username and user.password == password:
                return True
            return False


    @classmethod
    def find_user(cls, username):
        """find user using username"""
        for user in cls.user_accounts:
            if user.username == username:
                return user

    def save_user(self):
        """Append user to the user accounts lists"""
        User.user_accounts.append(self)

    @classmethod
    def display_user_accounts(cls):
        """Show all the user accounts in the array"""
        return cls.user_accounts

    def __repr__(self):
        return f'Fullname: {self.first_name} {self.last_name} Username: {self.username}'

