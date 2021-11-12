## Lab Exercise 11/18/2021 Problem 6
## Author: 
## Prime Factorization Program
from math import sqrt
def isPrime(number):
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def factor(number):
    factors = []
    if isPrime(number):     #need to handle the case of a number is prime
        factors.append(number)
        return factors
    for i in range(2, number):
        while number % i == 0:
            if isPrime(i):
                factors.append(i)
            number //= i
    return factors
    
number = int(input("Enter a number you want factored: "))
print ("The prime factors are: " + str(factor(number)))

##Sample Output
##Enter a number you want factored: 1234321
##The prime factors are: [11, 11, 101, 101]
