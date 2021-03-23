#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:58:57 2021

@author: suspect-0
"""

# let me try my own bubble sort


def selection_sort(L):
    suffix = 0
    while suffix != len(L):
        for i in range(suffix, len(L)):
            if L[suffix] > L[i]:
                # swap
                L[suffix], L[i] = L[i], L[suffix]
            
        suffix += 1
    return L

print(selection_sort([23, 3, 1, 8, 4, 2, 0, 5])) 