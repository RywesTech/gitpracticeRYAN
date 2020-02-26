# partner 1 Ryan Westcott
# partner 2 Aashni

# hello world Ryan

from random import random

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    rands=[]
    for i in range(n):
        rands.append(random())
    return rands

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product=1
    for entry in numbers:
        product=product*entry
    return product

def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
