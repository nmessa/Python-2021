# Lab Exercise 11.9.2021 Problem 4
# zeller.py
# Author: 
# This will determine the day of week for any date

#conversion dictionaries
monthNumber = {'01':11, '02':12, '03':1, '04':2, '05':3, '06':4, '07':5,
               '08':6, '09':7, '10':8, '11':9, '12':10}
monthName = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', \
             '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
dayName = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

#Get date from user (mm/dd/yyyy) and store in variable temp
#ADD YOUR CODE HERE


#break up the string to give month, day and year as a list of strings
#ADD YOUR CODE HERE


#in case user enters a 1 digit month concatenate a 0 in front of the digit
#ADD YOUR CODE HERE

    
#Extract month, day, and year from myDate (convert day and year to integers
#ADD YOUR CODE HERE


#Make calculations
#ADD YOUR CODE HERE




#Print the output
dayOfWeek = dayName[R]
print (monthName[myDate[0]]+ ' ' + myDate[1] + ','
       + myDate[2] + ' falls on ' + dayOfWeek)
