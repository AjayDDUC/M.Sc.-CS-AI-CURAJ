# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:24:33 2020

@author: AJAY
"""

"""
Problem:
    In this function we try to find out 
    pythongorean triplets upto 100.
Explanation: How to solve this problem
    (a,b,c) :
        a^2 + b^2 == c^2.
    (2m)^2 + (m^2-1)^2 == (m^2+1)^2
    
"""

def pythongorean_triplets(n):
    for m in range(2,n):
        a,b,c =  (2*m), (m**2-1), (m**2+1)
        if (a**2)+(b**2)==(c**2) and c<=n:
            print(a,b,c)

pythongorean_triplets(100)