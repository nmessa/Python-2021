## Lab Exercise 10/21/2021 Problem 2
## Author: 
## Silly sentence generator writing them to a file
## Files are stored in a text file with one element per line

from random import *

#open files and read to lists
#open adjectives.txt and read files to the list adjectives
myFile = open('adjectives.txt', 'r')
adjectives = myFile.readlines()
myFile.close()

#strip off newline characters
for i in range(len(adjectives)):
    adjectives[i] = adjectives[i].rstrip()
     
#open nouns.txt and read files to the list nouns
#Add code here



#open adverbPhrases.txt and read files to the list adverbPhrses
#Add code here

    

#open verbPhrases.txt and read files to the list verbPhrses
#Add code here



#Create the sentence
sentence = 'The ' + choice(adjectives) + " " + choice(nouns) + " " + \
           choice(verbPhrases) + " " + choice(adverbPhrases) + '\n'

#Print the sentence
print (sentence)



