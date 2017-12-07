#Name: Shiva Jaligama
#cs61002: Algorithm and Programming 1
#12/4/2016
#Lab07.py

import math
class vector(object):
    #defining constructor
    def __init__(ch, px,py):
        ch.px = px
        ch.py = py
    # getting vector values as string   
    def __str__(ch):
        return str(ch.px)+" "+str(ch.py)
    # adding two vectors c1 and c2
    def __add__(ch, other1):
        c1 = ch.px + other1.px
        c2 = ch.py + other1.py
        return(c1,c2)
    # subtracting two vectors c1 and c2
    def __sub__(ch, other2):
        c1 = ch.px - other2.px
        c2 = ch.py - other2.py
        return(c1,c2)
    # multiplying two vectors c1 and c2
    def __mul__(ch, other3):
        c1 = ch.px * other3.px
        c2 = ch.py * other3.py
        return(c1,c2)
    # magnitude of c1 and c2 vectors
    def magnitude(ch):
        c1 = ch.px * ch.px
        c2 = ch.py * ch.py
        return math.sqrt(c1 + c2)
    def scalar(ch, n):
        a = ch.px*n
        b = ch.py*n
        return a,b
        
n = 10
c1 = vector(5,10)
c2 = vector(4,5)

print 'Addition of two vectors: ', c1 + c2
print 'Subtraction of two vectors: ', c1 - c2
print 'Multiplication of two vectors: ', c1 *c2
print 'Magnitude of vector c1: ', c1.magnitude()
print 'Magnitude of vector c2: ', c2.magnitude()
print 'Magnitude of scalar vector c1: ', c1.scalar(10)
print 'Magnitude of scalar vector c2: ', c2.scalar(10)
