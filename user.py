class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'Fullname: {self.first_name} {self.last_name}\nUsername: {self.username}'

