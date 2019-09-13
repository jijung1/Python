# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:21:10 2019

@author: jin jung

Function that takes 2 lists of polynomial coefficients in the format: a+bx+cx^2+dx^3, ... => [a, b, c, d, ...]
And returns the product of the two polynomials
"""


def polyprod(p, q):
    size = len(p) + len(q) - 1
    res = [0]
    for i in range(size-1):
        res.append(0) 
        
    for j,k in enumerate(p):
        for m,n in enumerate(q):
            if j+m < size:
                if (p[j] < 0 or q[m] < 0): #check for negative coefficients
                    print("negative coefficient supplied. Result may be invalid.")
                    break;
                res[j+m] = (res[j+m] + p[j]*q[m]) % 256
                ++k
        ++j
    if res[size-1] == 0:
        del res[size-1]
    return res
    
print(polyprod([2,4,0,-1,5],[3,5,7]))
    