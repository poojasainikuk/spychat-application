# import statements
from globals import STATUS_MESSAGES
from termcolor import colored

# updated status message
updated_status_message = None


def add_status(current_status_message):
    if current_status_message != None:
        print 'your current status message is %s' % (current_status_message)
    else:
        print 'ypu do not have any status message currently \n'

        # ask user for choosing older message.
        default = raw_input("Do you want to select from the older status (y/n)? ")

        if default.upper() == "N":
            new_status_message = raw_input("what status message do you want to set?:\n")

            # validating user input.
            if len(new_status_message) > 0:
                # adding new status message.
                STATUS_MESSAGES.append(new_status_message)
                updated_status_message = new_status_message
                print 'your updated status message is: %s' % (updated_status_message)
            else:
                print "you didnot provide any status message . try again."
        elif default.upper() == "Y":
            # counter for serial no. of messages.
            item_position = 1

            # printing all older messages
            for message in STATUS_MESSAGES:
                print '%d. %s' % (item_position, message)
                item_position = item_position + 1

                # askig users choice.
            message_selection = int(raw_input("\nChoose from the above message \n"))

            # validating user input.
            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]
                print 'your updated status message is: %s' % (updated_status_message)
            else:
                print colored('invalid choice.try again.')
        else:
            print 'the option you choozse is invalid!'
        return updated_status_message