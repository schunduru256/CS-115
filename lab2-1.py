############################################################
# Name: Samhita Chunduru
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 2
#  
############################################################

def dot(L, K):
    "This function shows the output of the dot product between the lists L and K"
    if (len(L) == 0 or len(K) == 0):
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(s):
    "This function takes the string as an input and returns a list of characters"
    if (s == ""):
        return []
    else:
        return [s[0]] + explode(s[1:])
        
def ind(e, L):
    "This function takes the element e and sequence L"
    if (L ==[] or L == ""):
        return 0
    if (e == L[0]):
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e, L):
    "This function takes e and L and returns a list that's close to L"
    if (L == []):
        return []
    if (e == L[0]):
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    "This function takes a list L where all the values return true because of f"
    if (L == []):
        return []
    if (f(L[0]) == False):
        return myFilter(f, L[1:])
    else:
        return [L[0]] + myFilter(f, L[1:])

def deepReverse(L):
    "This function takes an input of an element that can also be a list in order to reverse the list"
    if (L == []):
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])
