'''Module for cleaning the screen'''
import os

os.system('cls')

class User:
    '''First class'''
    def __init__(self, user_id, username):
        self.ide = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        '''Method for followers'''
        user.follower += 1
        self.following +=1


user_1 = User("001", "Juan")
user_2 = User("002", "Diego")


user_1.follow(user_2)
print("Followers", user_1.follower)
print("Following", user_1.following)
print("---------")
print(user_2.follower)
print(user_2.following)
