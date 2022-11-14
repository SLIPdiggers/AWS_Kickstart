# AWS Restart Lab 8 - python
# 14/11/2022 - Ben Gladders
# Lab 8 - While Statements

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You Win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))

#psuedocode:
# while not guessed right
# ask user for a number between 1 and 10
# if the number they guessed is same as random - congratulate and exit loop
# otherwise, ask again and continue loop
#

for x in range (0, 11):
    print(x)

