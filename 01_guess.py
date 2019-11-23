lst = ["river", "dough", "grand", "match", "black", "shava"]

import random 

x = random.choice(lst)
first_letter = x[0]
print("Your word starts with ", first_letter, "! Take a guess!") 

count = 10

while count>0:
    guess = input("GUESS: ")
    if guess == "":
        print("You wasted a guess =P")
        count-=1
    elif len(guess) >5 or len(guess) <5:
        print("0, 1, 2, 3, 4, that's how we count to five!")
        count-=1
    elif len(guess) == 5 and guess[0] != x[0]:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        count = count
    elif guess == x:
        print("Good Job! You are one with the source!")
        break
    elif len(guess) == 5 and guess[0] == x[0]:
        print("You have ", count-1, "guesses left.")
        count-=1



