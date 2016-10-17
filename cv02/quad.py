#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP 2016 - cvičení číslo 2
"""


def is_convex(a, b, c, d):
    if  a == b or a == c or a == d:
        return False
    if  b == c or b == d:
        return False
    if  c == d:
        return False
    p0 = get_line(a,c)
    p1 = get_line(b,d)
    try:
        its =  get_intersection(p0,p1)
    except:
        return False
    
    if its[0] > a[0] and its[0] > c[0]:
        return False
    if its[1] > a[1] and its[1] > c[1]:
        return False
    if its[0] < a[0] and its[0] < c[0]:
        return False
    if its[1] < a[1] and its[1] < c[1]:
        return False
    if its[0] > b[0] and its[0] > d[0]:
        return False
    if its[1] > b[1] and its[1] > d[1]:
        return False
    if its[0] < b[0] and its[0] < d[0]:
        return False
    if its[1] < b[1] and its[1] < d[1]:
        return False
    return True
        

def get_intersection(a,b):
    """
    hleda prusecik a,b
    deleni nulou!
    """
    if a[2] == True:
        x = a[0]
    elif b[2] == True:
        x = b[0]
    else:
        x = (b[1]-a[1])/(a[0]-b[0])
    y = a[0]*x+a[1]
    return (x,y)
    

def get_line(a,b):
    '''
    vraci vzorec primky z usecky jako tuple(m, c, i) 
    podle schematu:
        if i==0:
            y=mx+c
        if i!=0:
            x=m
    '''  
    v0 = b[0]-a[0]
    v1 = b[1]-a[1]
    if v0 != 0:
        m = v1/v0
        if m == 0:
            m = 0
        
        return (m,a[1]-m*a[0],False)
    
    return (a[0],0, True)


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
