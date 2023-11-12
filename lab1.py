############################################################
# Name: Samhita Chunduru
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################
from math import factorial
from functools import reduce

"This function returns the reciprocal of the x value"
def inverse(x):
    return 1/x

"This function returns the sum of x and y"
def sum(x,y):
    return x + y

"This function returns the sum of the Taylor expansion using the factorials and inverse of each number in the list."
def e(n):
    list1 = range(0, n + 1)
    list1 = list(map(factorial, list1))
    list1 = list(map(inverse, list1))
    return reduce(sum, list1)
    
