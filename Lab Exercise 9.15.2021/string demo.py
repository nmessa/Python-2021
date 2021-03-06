## String Demo
## Author: nmessa
## Date: 9.20.2016

#create a test string
myString = "I saw a werewolf at Trader Vics, his hair was perfect"

#print the characters in the string one per line
print("This is the string printed one character per line")
for letter in myString:     #this is an implicit loop
    print(letter)

print()
print()

#print the string backwards
print("Original string:")
print(myString)
print("This is the string backwards")
length = len(myString)      #get the length of the string
for i in range(length-1, -1, -1):       #go through string from end to start
    print (myString[i], end = '')       #prints backward string on same line


print()
print()

#print only the vowels in the string
print("The string contains the following characters that are vowels")
vowels = 'aoeiou'
for letter in myString:
    if letter in vowels:
        print(letter, end = '')         #print vowels on same line

print()
print()

#demonstrate the end parameter of the print function
password = "hacker"
print("Here is a hacker with stars")
for letter in password:
    print(letter, end = '*')  #put a * after each letter

print()
print()

#Demonstrate upper and lower
newString = "Welcome to the Hotel California"
print("Here is a string in all lower case and all upper case")
print(newString.upper())
print(newString.lower())



        
