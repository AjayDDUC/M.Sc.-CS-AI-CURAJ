# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:24:00 2020

@author:    AJAY
"""

"""
Problem:
    HCF USING ECLID DIVISION LEMMA
EX:-
    According to Euclid Division Lemma, a = bq + r where 0 ≤ r ≤ b;


"""
import numpy as np

def HCF_Eclid_Division_Lemma(a,b):
    a = max(a,b)
    b = min(a,b)
    q = np.floor(a/b)
    r = a%b
    while r != 0:
        q = np.floor(a/b)
        r = a%b
        a = b*q+r
        a,b = b,r
        
    print("HCF",a)


HCF_Eclid_Division_Lemma(250,75)