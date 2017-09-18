#import statements
from globals import friends
from termcolor import colored

#add new friend.
def add_friend() :
    new_friend = {
        'name' : '',
        'salutation' : '',
        'age' : 0,
        'rating' : 0.0,
        'is_online' : False
    }

    new.name = raw_input("please add your friend's name: ")
    new.salutation = raw_input("are they Mr. or Ms.? ")
    #concatenation
    new_friend.name = new_friend.salutation + " " +  new_friend.name

    new_friend.age = int(raw_input("Age? "))

    new_friend.rating = float(raw_input("Spy rating? "))


    #user input validations
    if len(new_friend.name) > 0 and new_friend.age >12 and new_friend.age < 50:
        new_friend.is_online = True
        friends.append(new_friend)
        print colored('Friend added!')
    else:
        print 'Sorry,invalid entery'

        #returing total no. of friends
    return len(friends)
