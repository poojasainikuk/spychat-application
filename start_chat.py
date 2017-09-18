#import statement
#from globals import current_status_message
from add_friend import add_friend
from add_status import add_status
from select_friend import select_friend

#start chat funtion defination.
def start_chat(name, age, rating, status):
    from globals import current_status_message
    #validating users details.

    error_message = None #variable for storingerror message

    if not (age > 12 and age < 50):
        #invalid age.
        error_message = "Invalid age. Provide correct details."
        print error_message
    else:
        welcome_message = "Authentication complete . welcome \n Name : " + name + "\nAge: " + str(age) + " \nRating: " + str(rating) + "\nProud to have you onboard"
        print welcome_message

         #displaying menu for user

        show_menu = True
        while show_menu:
            menu_choices = "What do you wamt to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secert message \n 4. Read a secret message \n 5. Read chat from a user \n 6. Close the application \n  "

            result = int(raw_input(menu_choices))
              #condions checking

            if (result == 1):
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                number_of_friends = add_friend()
                print 'you have %d friends' % (number_of_friends)
            elif (result == 3):
                select_friend()
            elif(result == 6):
                  #close application
                show_menu = False
            else:
                print "wrong choice try again."