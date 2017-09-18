# details of default user
from datetime import datetime
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('pooja', 'Ms.', 21, 4.7)


friend_one = Spy('deep', 'Mr.',21, 4.8)
friend_two = Spy('adi', 'Ms.',21, 4.8)
friends = [friend_one, friend_two]

class Chat:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

