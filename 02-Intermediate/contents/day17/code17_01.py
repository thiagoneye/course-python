"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 17
Working with attributes, class, constructors and the __init__() function
"""


class User:
    # pass  # Reserved word used in empty scoped classes or functions

    def __init__(self, user_id, name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1  # This resource is amazing!
        self.following += 1


user1 = User('001', 'Mary')
user2 = User('002', 'John')

print(user1.username)

user1.follow(user2)

print(f'{user1.username} (user 1) follows {user1.following} users and has {user1.followers} followers .')
print(f'{user2.username} (user 2) follows {user2.following} users and has {user2.followers} followers .')