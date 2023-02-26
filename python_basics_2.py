# *****************************************************************************************************
# session 2 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here 
#     - strings
#     - input function
#     - while loops
#     - int conversion
#     - negation

# CONCEPT : input()
# EXPLANATION : 
# - it's another function, just like print
# - it's the way we ask users to insert data from keyboard
# - the function will print the string it gets as a parameter 
#     and wait for the user to insert something from the keyboard
# CODE EXAMPLE :
a = input()
b = input("insert nr: ")

# CONCEPT : strings
# EXPLANATION : 
# - literaly a string of characters
# - a type of data we can use to assign to variables and do fun things with
# - like passing it to functions like print and input
# CODE EXAMPLE :
a = "this is a string"
b = 'this is also a string'
print(a)
print(b)
print("yet another string")

# RECAP from last time
 
# EXERCISE : 1 
# - what will the following program print and why
# - play around with it and try to explain it
# - what was the difference between = and ==
# code section 
a = input("insert a number")
b = input("insert another number")
print(a == b)

# EXERCISE : 2
# - what will the following program print
# code section 
print(7 % 3)

# EXERCISE : 3
# - what will the following program print
# code section 
print(7 // 3)

# EXERCISE : 4
# - what will the following program print
# code section 
print(7 <= 3)

# MENTOR NOTE: errors, the bane of all programmers
# - In the next exercise i'd let them let get the conversion error first 
    # it's got a pretty good message for a first time error
    # and then explain that input returns a string 
    # even if they put in a number and that we need to convert
# EXERCISE : 5
# - check if a number given by a user is divisible by 10
# code section 
a = int(input("insert a number"))
if a % 10 == 0:
    print(True)
else:
    print(False)

# EXERCISE : 6
# - check if one number is greater than the other 
    # if they are print the difference of the numbers 
    # otherwise if the number is lesser than the other 
    # print the sum of the numbers
    # else print "the numbers are equal"
# code section
a = int(input("insert a number"))
b = int(input("insert a number"))
if a > b:
    print (a - b)
elif a < b:
    print (a + b)
else:
    print("the numbers are equal")

# CONCEPT : while loops
# EXPLANATION : 
# Think of a while loop like a game where you have a task to complete. 
# For example, imagine you have to take out 5 apples from a large barrel. 
# You would start by taking an apple out the basket, counting it and set it aside. 
# Then, you would take another one count it and set it aside. 
# You would keep doing this until you took out 5 apples.
# How would this look like in code.
# CODE EXAMPLE :
# general form 
# while statement:
#     codeblock
# statement is the same as the conditions we have discussed with if
# we can operations like >, <, ==, or anything that will return true or false
# CODE EXAMPLE :
b = int(input("number of apples in the barrel"))
a = 0
while a < 5 :
    b = b - 1 # taking apple out of barrel 
    a = a + 1 # counting and setting aside
    print(" took out one apple ")
print(" we got 5 apples ")

# EXPLANATION :
# how would it look like without a loop
b = int(input("number of apples in the barrel"))
a = 0

# 1 apple
b = b - 1 # taking apple out of barrel 
a = a + 1 # counting and setting aside
print(" took out one apple ")

# 2 apple
b = b - 1 # taking apple out of barrel 
a = a + 1 # counting and setting aside
print(" took out one apple ")

# 3 apple
b = b - 1 # taking apple out of barrel 
a = a + 1 # counting and setting aside
print(" took out one apple ")

# 4 apple
b = b - 1 # taking apple out of barrel 
a = a + 1 # counting and setting aside
print(" took out one apple ")

# 5 apple
b = b - 1 # taking apple out of barrel 
a = a + 1 # counting and setting aside
print(" took out one apple ")

# as you can see it takes a lot of code to get the same result without loops
# loops are verry powerfull tools this is just a simple example
# imagine executing lines of code milions of times or if you make a mistake forever
# if we are not carefull with the condition we set in the while our loop may never end
# CODE EXAMPLE : 
b = int(input("number of apples in the barrel"))
a = 0
while a < 5 :
    b = b - 1 # taking apple out of barrel 
    print(" took out one apple ")
print(" we got 5 apples ")
# the loop above will run forever since we forgot to increment a so it will forever be < 5
# MENTOR NOTE : go through with the example and show them how to kill the program (CTRL + C)

# Armed with new and powerfull code magic it's time to practice

# EXERCISE 7 :
# count from 1 to 1.000.000
# code section 
a = 0
while a < 1000000 :
    a = a + 1
    print(a)

# EXERCISE 8 : 
# ask for a number and print your name that manny times
# code section
a = int(input(" insert a number "))
b = 0
while b < a :
    b = b + 1
    print("My name is ...") 

# EXERCISE 9 :
# ask for two numbers, first one greater that the seccond
# multiply the seccond one with 3 until it's greater than the first number
# code section
a = int(input(" insert a number "))
b = int(input(" insert a number "))
while b < a :
    b = b * 3

# EXERCISE 10 : 
# taking the code from the last exercise 
# check if the number you got from the loop is even
# if it is print it
# if it is not print the message "try again"
# print the number of times you had to multiply it
# code section
a = int(input(" insert a number "))
b = int(input(" insert a number "))
c = 0
while b < a :
    b = b * 3
    c = c + 1
if b % 2 == 0 :
    print(b)
else : 
    print("try again")
print(c)

# CONCEPT : negation 
# EXPLANATION :
# Until now, with our loops we have only done things while our contion is true
# if our condition was false we would leave the loop or not enter it in the first place
# what if we want to reverse things and execute code in a loop 
# but only while our condition is false, if it's true we want to end the loop.
# when might this be usefull, we have a nice example in the next exercise.
# Until then let's learn about not or !
# not or ! is a logical operator, like and, or that can be used only with statements
# that are true or false for example if is something equal to something else.
# code section
a = True
print(a)
print(not a)
b = False
print(b)
print(not b)
print(a == b)
print(a != b)

# Exercise 11 :
# ask for the user to input numbers and print them untill he inputs the number 6
# code section
a = 0
while a != 6 :
    a = int(input("insert any number, 6 to exit"))
    print(a)

# Exercise 12 :
# ask for the user for numbers until 6 is inserted
# calculate the average of the numbers
# code section
a = 0
s = 0
n = 0
while a != 6 :
    a = int(input("insert any number, 6 to exit"))
    s = s + a
    n = n + 1
print(s/n)