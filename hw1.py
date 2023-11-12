############################################################
# Name: Samhita Chunduru
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 HW 1
#  
############################################################

from functools import reduce

def mult(x, y):
    "This function returns the product of x and y"
    return x * y

def add(x, y):
    "This function returns the sum of x and y"
    sum = x + y
    return(sum)

def factorial(n):
    "This function returns the  factorials of the given n"
    return reduce(mult, range(1, n+1))

def mean(L):
    "This function finds the mean of the list"
    return reduce(add, L)/(len(L))
