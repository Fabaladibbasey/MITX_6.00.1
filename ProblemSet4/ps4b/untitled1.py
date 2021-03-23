#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:14:48 2021

@author: suspect-0
"""

# def genSubSet(L):
#     if len(L) == 0:
#         return [[]]
    
#     smaller = genSubSet(L[:-1])
#     # print(smaller)
#     # print('Start another one')
#     extra = L[-1:]
#     # print(extra)
    
#     for small in smaller:
#         print(small)




def genSubsets(L): 
    # res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without
    # last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        print(small)
        new.append(small+extra) # for all smaller
    # solutions, add one with last element
    return smaller+new # combine those with last
    # element and those without
l = [2, 4, 6]
genSubsets(l)