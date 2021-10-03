##Lab Exercise 10/8/2021 Problem 5
##mersenne.py
##Author: 
##This program will find the first 8 Mersenne Primes

from math import *

#This function returns True if passed a prime number
def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

#This function returns True if passed a Mersenne Prime number
def isMersenne(n):
    #Add code here

    

#Create list to hold the Mercenne Prime numbers and the prime number
#that generated them
mersennes = []
numbers = []


for number in range(2,1000):
    if not isPrime(number):
        continue  #don't test for Mercenne Prime if number is not prime
    if isMersenne(number):
        mersennes.append(number) #put prime number in list of primes tested
    if len(mersennes) == 8:  #leave loop if you have 8 Mercenne Primes
        break

#Print the list showing the Mercenne Prime and the prime
#number that generated it.
for i in range(len(mersennes)):
    print("p =", mersennes[i], "Mersenne Prime Number =", numbers[i])
    
##Output
##p = 2 Mersenne Prime Number = 3
##p = 3 Mersenne Prime Number = 7
##p = 5 Mersenne Prime Number = 31
##p = 7 Mersenne Prime Number = 127
##p = 13 Mersenne Prime Number = 8191
##p = 17 Mersenne Prime Number = 131071
##p = 19 Mersenne Prime Number = 524287
##p = 31 Mersenne Prime Number = 2147483647
