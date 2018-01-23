import random

print('-----------------------------------------')
print('         GUESS THAT NUMBER GAME          ')
print('-----------------------------------------')
print()


the_num = random.randint(0,50)

user_int = -1

while user_int != the_num:

    user_text = input("Enter an integer between 0 and 100 ")
    user_int = int(user_text)

    if user_int == the_num:
        print("That's it the number was {0}!" .format(user_int))
        # We could have also used user_text or + str(user_int) but we wanted to illustrate the .format method
    elif user_int < the_num:
        print("Your guess of {0} was too LOW".format(user_int))
    else:
        print("Your guess of {0} was Too HIGH".format(user_int))




