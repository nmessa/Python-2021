##Lab Exercise 9/24/2021 Problem 2
##Author: 
##This program generates a list of 1000 elements
##The list contains random integers ranging from 1 to 10000
##The program will then calculate the following descriptive statistics:
## mean
## median
## maximum
## minimum
## range

import random

#this function will calculate and return the mean of the data in the list
def calcMean(nums):
    mean = sum(nums)/len(nums)
    return mean

#this function will return the median of the data in the list
def findMedian(nums):
    #Add code here
    

#this function returns the maximum value of the data in the list
def findLargest(nums):
    #assumes sorted list
    #Add code here

    

#this function returns the minimum value of the data in the list
def findSmallest(nums):
    #assumes sorted list
    #Add code here
    

#this function returns the range of the data in the list
def findRange(nums):
    return findLargest(nums) - findSmallest(nums)

#create an empty list
#Add code here
    

#generate list
#Add code here
    

#uncomment this code to print the list in 10 columns
##for i in range(len(numbers)):
##    print numbers[i], '  ',
##    if i % 10 == 0:
##        print

#sort the list
#Add code here
    

print ('Mean =', calcMean(numbers))
print ('Median =', findMedian(numbers))
print ('Maximum value =', findLargest(numbers))
print ('Minimum value =', findSmallest(numbers))
print ('Range =', findRange(numbers))

## Output
## Mean = 4892.942
## Median = 5019.0
## Maximum value = 9991
## Minimum value = 1
## Range = 9990
