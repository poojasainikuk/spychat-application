from spy_details import Chat,friends
from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
from tremcolor import colored



def send_message():
    sender = select_friend()
    output_path = raw_input(colored("enter the name of file in which message is hidden?", 'grren'))
    try:
        secret_text = Steganography.decode(output_path)
    except ValueError:
        print colored("no srcret message is decoded!!", 'blue')
        exit()

    secret_text = str(secret_text)
    if secret_text == 'None':
        print colored("no srcret message is decoded!!", 'blue')
    else:
        if len(secret_text) > 100:
            print colored("your friend talked",'black')
            choice = raw_input(colored("if you want to delete your friend: "Y", if not: "N" "))
            if choice == "Y"
                del [sender]
                print colored("friend not in friend list", 'red')
                print colored("select from below given friend", 'brown')
            else:
                print colored("secret_text", 'green')
        else:
            #save the data
            new_chat = {
            "message" : secret_text,
            "time" : datetime.now(),
            "sent_by_me" : False
            }
            print colored("your message been saved,", 'yellow')

    friends[sender]['chats'].append(new_chat)
    print "your secret message  has been saved."