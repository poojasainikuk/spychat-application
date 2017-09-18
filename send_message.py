from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
import re
from termcolor import colored



def send_message():
    friend_choice = select_friend()

    original_image = raw_input(colored("enter the name of image to hide the message : ",'blue'))
    pattern = '^[0-9a-zA-Z\s]+\.jpg$'
    if(re.match(pattern, original_image) != None):
        output_image = raw_input("enter name of output image: ")
        text = raw_input("enter your message :")

        # encrypt the message
        Steganography.encode(original_image, output_image, text)
        new_chat = {
            "message": text,
            "date and time": datetime.now(),
            "sent_by_me": True
        }

        friends[friend_choice]['chats'].append(new_chat)
        print colored("your secret message  has been saved.",'yellow')

