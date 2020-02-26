# partner 1 Ryan Westcott
# partner 2 Aashni

# hello world Ryan

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    pass

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product=1
    for entry in numbers:
        product=product*entry
    return product

def main():
    print(multiplyRandom([1,5,3,2,8]))
#   print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
