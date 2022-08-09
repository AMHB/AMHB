from ast import Break
from ast import Continue
#from pickle import TRUE
import random
checker = 0
i = 1
j=99
while True:

    guess = random.randint(i,j)
    if guess != checker:
        print (guess)
      
    else:
        guess = random.randint(i,j)
        print (guess)

    checker = guess

    status = input("Please Clarify the status of guessed Number with k,b or d      ")
    if status == "k":
        j = guess
        continue
    if status == "b":
        i = guess
        continue
    if status == "d":
        print("Yessss your guess is correct!!!")
        break
