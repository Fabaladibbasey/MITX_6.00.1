#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:26:55 2021

@author: suspect-0
"""

# def intToStr(i):
#     digits = '0123456789'
#     if i == 0:
#         return '0'
#     result = ''
#     while i > 0:
#         print(result)
#         result = digits[i%10] + result
#         i = i//10
#     return result



def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
          
        if not matched:
            return False
    return True



def genSubsets(L):
    # res = []
    print('L', L)
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    print('the smaller', smaller)
    extra = L[-1:] # create a list of just last element
    print('last element', extra)
    new = []
    for small in smaller:
        print('small', small)
        print('new', new)
        new.append(small+extra) # for all smallersolutions, add one with last element
    return smaller+new # combine those with last element and those without

l1 = [2, 4, 6]
# l2 = [1, 2, 3, 4, 5, 6, 7]

print(genSubsets(l1))






