#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 07:39:40 2021

@author: suspect-0
"""

# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print("Unknown verb {}".format(verb_word))
#         return
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("Nothing"))
        

# def say(nound):
#     return 'You said "{}"'.format(nound)

# verb_dict = {
#     "say": say
#     }


# while True:
#     get_input()





class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @property
    def pineapple_allowed(self):
        return False
    
    

pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)



class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w = Weird(X, Y)

        
        
        
        
        
        
        
        
        