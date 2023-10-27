#Task: Below are the steps:

"""Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
print("Number Guessing Game")
num = random.randint(1, 100)
print(num)
count=0
while True:
    guess=int(input("Enter a num: "))
    if guess<num:
        print("Two low")
    elif guess>num:
        print("Two high")
    elif num==guess:
        print("Correct Answer")
        print("Done")
        break
    count=count+1
print(f'How many attempts {count}') """


"""In this game, there is a list of words present, out of which our interpreter will choose 1 random word.
 The user first has to input their names and then, will be asked to guess any alphabet. 
 If the random word contains that alphabet, it will be shown as the output(with correct placement) 
 else the program will ask you to guess another alphabet. 
 The user will be given 12 turns(which can be changed accordingly) to guess the complete word."""

import random

print("Word Guessing game")
List = ["apple", "orange", "Grapes", "Banana"]
x = random.choice(List).lower()  # Convert the word to lowercase for case-insensitive comparison
print(x)

count = 0
while True:
    guess = input("Enter a letter: ").lower()  # Convert the guess to lowercase for case-insensitive comparison
    if x==List[0]:
        print(len(x))

print(f'Total Attempts: {count}')



