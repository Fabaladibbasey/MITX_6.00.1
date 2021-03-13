#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:36:57 2021

@author: suspect-0
"""

import string
def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # pass #delete this line and replace with your code here
        dic = {}
        lowerAlphabets = string.ascii_lowercase
        shiftedLowerAlphabets = lowerAlphabets[shift:] + lowerAlphabets[:shift]
        upperAlphabets = string.ascii_uppercase
        shiftedUpperAlphabets = upperAlphabets[shift:] + upperAlphabets[:shift]

        
        # adding lowerCase to the dic
        for i in range(len(lowerAlphabets)):
            lowerKey = lowerAlphabets[i]
            lowerValue = shiftedLowerAlphabets[i]
            dic[lowerKey] = lowerValue
            
            
        # adding upperCase to the dic
        for i in range(len(upperAlphabets)):
            upperKey = upperAlphabets[i]
            upperValue = shiftedUpperAlphabets[i]
            dic[upperKey] = upperValue
             
        return dic
    
def apply_shift(shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        encryptValues = build_shift_dict(7)
        encryptedStr = ''
        print(encryptValues)
        print(shift)
        for letter in shift:
            encryptLetter = encryptValues.get(letter, 0)
            if encryptLetter != 0:
                encryptedStr += encryptLetter
            else:
                encryptedStr += letter
                
        print(encryptedStr)
        
        return encryptedStr
        
        
        
apply_shift("this is Problem Set 6?")







