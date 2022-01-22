class User:
    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):
        # Append user to the user accounts lists
        User.user_accounts.append(self)

    @classmethod
    def get_user_accounts(cls):
        return cls.user_accounts

    def __repr__(self):
        return f'Fullname: {self.first_name} {self.last_name}\nUsername: {self.username}'

