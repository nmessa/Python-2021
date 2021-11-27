## Lab Exercise 12/2/2021 Pin Cipher
## Author: 
## This is a Julius Ceasar cipher for PIN numbers

def PINCypher(pin, shift):
    cypherText = ""
    
    #Add code here

    
    return cypherText   

#Test code
pin = '12345'
shift = 1
print (PINCypher(pin, shift)) #23456
shift = 6
print (PINCypher(pin, shift)) #78901
shift = 23
print (PINCypher(pin, shift)) #45678
shift = -1
print (PINCypher(pin, shift)) #01234
