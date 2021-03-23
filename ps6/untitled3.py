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


def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
    #     for i in range(1, 27):
            
    #     splitedWords = self.message_text.split(" ")
    #     resultList = []

    #     for eachWord in splitedWords:
    #         self.message_text = eachWord
    #         aWord = self.the_word(self.message_text)
    #         aWord = is_word(aWord)
    #         resultList.append(aWord)
    #         print(aWord)
            
    #     print(resultList)

    #     print('ohhh' , self.the_word(aWord))
        
    # def the_word(self, word):
        
    #     word_list = self.get_valid_words()
    #     for i in range(26, -1, -1):
            
    #         if word.lower() in word_list:
    #             return i, word
    #         word = self.apply_shift(i)
    
    #     return i, word
        
    



