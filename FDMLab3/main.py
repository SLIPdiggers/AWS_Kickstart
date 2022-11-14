# AWS Restart Lab 3 - python
# 14/11/2022 - Ben Gladders
# Lab 3 - Strings and input()

myString = "This is a string."
print(myString)

print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name?: ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name, color, animal))

