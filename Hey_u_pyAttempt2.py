# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:54:38 2023
@author: segal
"""
# start with an outline
'''
First a few comments:
# ask user for name
# ask user for their age
# ask user for city
# ask user what they like doing
plus create output txt
and
print output to screen
'''
givenName = input("What's your name bro? \n")

Age = input("How old are u dude? \n")

city = input("What's your city? \n")

hobbies = input("What do you like doing? \n")

# creating the output txt:
string = "Your name is {} and you are {} year old. And you live in {}. Plus you like {}."

# the printing the output to the screen:
outputing = string.format(givenName, Age, city, hobbies)    
print(outputing)

# and like string formating to use:
    


