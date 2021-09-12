#Times tables drill program
#Includes timer, multiple problems, and scoring
#Author: nmessa
import random, time

numCorrect = 0
problems = int(input("How many problems do you wish? "))

#Loop number of problems times
for i in range(problems):
#Generate two random numbers
    number1 = random.randint(1, 12)
    number2 = random.randint(1, 12)

#Get answer from user
    print ("What is " + str(number1) + " x " + str(number2) + "?")
    
#Check time to answer problem
    start = time.time()
    answer = int(input())
    stop = time.time()
    if stop - start > 5:
        print ("Took too long")
        answer = 0

#Check answer for correctness
    if answer == number1 * number2:
        print ("Correct")
        numCorrect += 1
    else:
        print ("Study harder")

#Calculate percentage
percentage = 100 * round(numCorrect/problems, 2)
print (str(percentage) + "%")

#Determine grade
if percentage >= 90:
    print ("A")
elif percentage >= 80:
    print ("B")
elif percentage >= 70:
    print ("C")
elif percentage >= 60:
    print ("D")
else:
    print ("F")
