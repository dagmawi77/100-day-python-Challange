class User:

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.follower = 0


userOne = User("Dagmawi", "dagmawiletarik@gmail.com")
print(f"The user name: {userOne.user_name} \nEmail Address : {userOne.email} \nFollower : {userOne.follower}")



