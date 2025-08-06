
import random
selected_num = random.randint(1,10)
guess = int(input("Pick a number from 1 to 10, lets see if you get it right!"))
if selected_num == guess:
    print("You are right!")
else:
    print("You are Wrong")

