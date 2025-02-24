#{NUMBER GUESSING GAME}

import random

#step1
random_number = random.randint(1,100)

#step2
user_input = int(input("Enter Number: "))

#step3
if user_input < random_number:
 print("too low")
elif user_input > random_number:
 print("too high")
else:
  print("correct number")
