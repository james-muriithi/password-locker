from user import User

user1 = User("James", "Muriithi", "james-muriithi", "password")
user2 = User("James2", "Muriithi2", "james-muriithi2", "password")

user1.save_user()
user2.save_user();

print(User.user_accounts)