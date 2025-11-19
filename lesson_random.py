# import random
# from random import *
# from random import randint, randrange 
# from random import randint as ri

import random as r

comp_choice = r.randint(0, 100)
counter = 0

while True:
    counter += 1
    try:
        num = int(input("Input number 1-100 :"))
    except ValueError:
        print("Incorrect symbol")
        continue
    else:
        print("Excelent! I remember your number")
    finally:
        print(f"Your attempt is {counter}\n")

    if num == comp_choice:
        print("You win!!!!!")
        break
    elif num > comp_choice:
        print("Your number is more than ours. Try again!\n")
        continue
    else:
        print("Your number is less than ours. Try again!\n")
        continue
