#import statements
from globals import friends

#defination to select a friend

def select_friend():
 #use counter to add a number of friend
    counter = 1
    for friend in friends:
        print str(counter) + " . " + friend['salutation'] + " " + friend['name']
        counter += 1

        #for choosing a friend from the list
    user_input = int(raw_input(" Choose the friend from the list :"))
    if user_input <= counter:
        return user_input - 1
    else:
        print " invalid choice.Try again."
        exit(-1)
