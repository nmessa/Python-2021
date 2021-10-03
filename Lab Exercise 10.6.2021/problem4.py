## Lab Exercise 10/6/2021 Problem 4
## Author: 
## This program will validate a password

#This function will test a password for adequate security
def isValid(password):
    #initialize counters
    uc = 0
    lc = 0
    dig = 0
    
    #check for length
    #Add code here
    


    #Check each character for uppercase, lowercase, and digit characters
    #Add code here

    

    #if correct number of uppercase, lowercase, and digit characters
    #return True or else return False
    #Add code here
    

#test code for isValid function
##print isValid('test') #False - too short
##print isValid('abcdefgh') #False no upper case no digit
##print isValid('abcDefgh') #False no digit
##print isValid('ab2defgh') #False no upper case
##print isValid('abCde3gh') #True

#Print user instructions
print("Enter your password twice")
print('Your password must contain at least 8 characters')
print('It must contain at least 1 upper case, 1 lower case, and 1 digit')


valid = False   

#Test the password algorithm
while not valid:
    password = input("Enter a password: ")
    if isValid(password):
        password2 = input("Enter your password again: ")
        if password == password2:
            print ("Valid password")
            valid = True
        else:
            print ("Passwords do not match")
    else:
        print ("Password does not meet security requirements")
