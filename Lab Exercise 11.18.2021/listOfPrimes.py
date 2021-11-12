## Lab Exercise 11/18/2021 Problem 5
## Author: 
## Prime List
from math import sqrt

def isPrime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def listOfPrimes(number):
    primeList = []
    #Add prime numbers to the primeList
    #Add code here
    
        
    return primeList
    
number = int(input("Enter the largest prime to check: "))
print ("The prime numbers are: " + str(listOfPrimes(number)))
