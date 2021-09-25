#Demonstration of use of modules
#Author: 
#Date: 9.29.2021

import my_module
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print ("That's", fahrenheit, "degrees Fahrenheit")

#Uncomment the following 3 lines once you have added the f_to_c function to my_module
##fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
##celsius = my_module.f_to_c(fahrenheit)
##print ("That's", celsius, "degrees Celsius")

##Sample Output
##Enter a temperature in Celsius: 100
##That's 212.0 degrees Fahrenheit
##Enter a temperature in Fahrenheit: 212
##That's 100.0 degrees Celsius
