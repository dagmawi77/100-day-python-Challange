class User:

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.followers = 0
        self.following = 0
# Adding Methods
    def follower(self, user):
        user.followers += 1
        self.following += 1
#adding  comment



userOne = User("Dagmawi", "dagmawiletarik@gmail.com")
print(f"The user name: {userOne.user_name} \nEmail Address : {userOne.email} \nFollower : {userOne.follower}")

userTwo = User("Abebe", "abebe@gmail.com")

userOne.follower(userTwo)

print(userOne.followers)
print(userOne.following)
print(userTwo.followers)
print(userTwo.following)





