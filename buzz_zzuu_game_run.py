from buzz_zzuu_game_functions import *

while True:
    user_input = input("Put in a number")
    if bizzzuu(int(user_input)) is True:
        print('bizzzuu')
    elif buzz(int(user_input)) is True:
        print("buzz")
    elif zzuu(int(user_input)) is True:
        print("zzuu")
    elif user_input == '-1':
        break
print("Thanks for playing!")