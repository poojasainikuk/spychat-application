#import details
from spy_details import spy
from start_chat import start_chat
import re

print "Let\'s get started...."
question = "Do you want to continue as " + spy.salutation  + " " + spy.name + " (Y/N) : "
existing = raw_input(question)

 #validating users input

if(existing.upper() == "Y") :
     #user want to continue as default user

     #concatenation aof salutation and name of spy
    spy.name = spy.salutation  + " " + spy.name

     #starting chat application
    start_chat(spy.name, spy.age,  spy.rating, spy.is_online)
elif (existing.upper == "N") :
     #user want to continue as a new user
    spy.name = raw_input("Provide your name here :")
     #check whether spy has enterd some input or not
    if len(spy.name) > 0 :
        #input more details about user
        name_pattern = '^[a-zA-Z]+\s*[a-zA-Z\s]+*$'#spy name contain alphabets only
        if(re.match(name_pattern, spy.name) != None):
            spy.salutation = raw_input('what should we call you ? :')
            print 'Wlcome!, spy.salutation + " " +  spy.name . we are glad to have you back with not us'
            spy.age = int(raw_input("Enter your age?")) #typecasting
            age_pattern = '^[0-9]{1,3}$' #three digit maximum value is allowed
            if (re.match(age_pattern,spy.age) != None):

                spy.age = int(spy.age)

                if int(spy.age) > 12 and int(spy.age) < 50:
                    spy.rating = float(raw_input(" What is your spy rating?"))  # typecasting
                    rating_pattern = '^[0-9]{1-2}[.][0-9]{1}$'
                    if (re.match(rating_pattern, spy.rating) != None):
                        spy.rating = float(spy.rating)

                        if (float(spy.rating) >= 0.0) and (float(spy.rating) <= 5.0):
                            spy.is_online = True

                        # starting chat application
                            start_chat(spy.name, spy.age, spy.rating, spy.is_online)

                            if (float(spy.rating) >= 1.0) and (float(spy.rating) <= 2.0):
                                print 'you are good!'
                            elif (float(spy.rating) >= 2.0) and (float(spy.rating) <= 4.0):
                                print 'you are very good!,appricible'
                            elif (float(spy.rating) >= 4.0) and (float(spy.rating) <= 5.0):
                                print 'you are very good!,awesome'
                elif int(spy.age <12):

                    print 'you are too young to join' + spy['name']
                elif int(spy.age > 50):

                    print 'you are too young to old,sorry' + spy['name']
            else:
                print 'enter valid age,'

    else:
        print " Wrong choice.Try again."
