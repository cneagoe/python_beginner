# python basics
# *****************************************************************************************************
# session 1 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here
#     - variables
#     - int data type
#     - basic math operators
#     - bool data type
#     - basic logical operators 
#     - if statements
# take this session to calibrate, if it's easier you can record it and review after
# important things to keep in mind
#     - how long does a regular exercise take to cover with each kid,
#         it will help with exercise selection and keeping things on track going forward
#     - what is the actual knowledge level of the kids, keep in mind this varries a lot
#         they can be self taught, parrent taught, tutored, taught in class,
#         try to stay objective, you will get an even better feel for their capabilities
#         as the sessions progress
# time, we only have so much of
#     - don't over do it on the first session, try to stay under two hours with a couple of
#         breaks in between, they are kids and they'll get tired well before you will
#         also it's nice to be consistent so try to figure out a chunk of time you can 
#         reliably spend every week with them at the minimum (ideally min is 1h 30min)
#         more time spent with the kids is of course welcomed, 
#         the more you give the better you'll feel (endorfins righ! heluva drug :D)
# time for practice
#     - there will be 12 exercises for the first tier, they are not mandatory, 
#         but a nice target for the first session would be to get each kid to present his screen 
#             and work on an exercise then move on to the next kid and do the same, try to do this twice
#     - ideally you should spend around 5 min per each kid or less to get two exercise each, 
#         nothing wrong with taking around 10 and doing only one exercise each 
#         (numbers are based on 6 kids per group, adjust accordingly)
#     - try to get each of the kids to share their screen as you work with them through the exercises, 
#         it will keep them engaged and paying attention to what is going on
#         they will appreciate the attention and you will feel all worm and fuzzy on the inside
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CONCEPT : Variables
# DEFINITION : A container we use to keep information in. ( bucket/ cardboard box analogy, whatever gets the point across)
# CODE EXAMPLE :   
a = 6 
print(a)

# EXPLANATION :
# - How would we put in words what we just wrote
#     - the variable named "a" takes the value of (=) the number 6 
# - what is a 
#     - it's the name of the variable (can be pretty much everything)
# - what is =
#     - it's an operator (we use it to do math and things similar to math)
# - what is 6
#     - it's a number
#     - What is a number 
#         - a type of variable
#         - we'll learn about a few more variable types by the end of this course
#         - you may already know about strings for example
#     - there are two tipes of numbers we'll work with throught this course
#     - int (ex: 2 3 45 829)
#     - float (ex: 3.8 5.2 834.56)
#     - for now we'll focus more on int numbers
 
# CONCEPT : functions
# DEFINITION : 
# In Python, a function is a block of code that performs a specific task. 
# It can take one or more inputs, called parameters, and return a value as output. 
# Parameters are like the ingredients you might put into a recipe. 
# They're values that you pass into the function, and the function uses them 
# to perform some kind of operation.

# CONCEPT : print()
# EXPLANATION :
# The print function tells the computer to display some text on the screen. 
# It's like a magic spell that makes words and numbers appear out of thin air! 

# CONCEPT: Mathematical operations
# EXPLANATION : Same things you were taught in math class, addition, subtraction, 
#     multiplication, division, and a couple more new ones like modulus and integer division.
#     Why do math when we can have computers to do it for us.
    
# CODE EXAMPLE : addition
a = 6 
b = 7
c = a + b
print(c)
		
# CODE EXAMPLE : subtraction
a = 15 
b = 8
c = a - b
print(c)

# CODE EXAMPLE : multiplication
a = 15 
b = 23
c = a * b
print(c)

# CODE EXAMPLE : division
a = 27 
b = 3
c = a / b
print(c)

# CODE EXAMPLE : mod()
a = 7 
b = 3
c = a % b
print(c)

# EXPLANATION : returns the rest of the division

# OPTIONAL :
# - why is modulo a thing and why we need it (huge rabit hole)
# - just one example
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)
# https://goteleport.com/blog/comparing-ssh-keys/

# OPTIONAL CONSOLE EXAMPLE :
# 5 / 2 = 2.5
# 5 // 2 = 2
# CODE EXAMPLE : integer division
a = 7 
b = 3
c = a // b
print(c)

# EXPLANATION : returns the division resust rounded down to nearest integer

# CONCEPT : if statement
# DEFINITION : Statement that allows us to perform actions only when certain conditions are met.
# GENERIC FORM :
# if statement:
#     code_block
# elif another_statement:
#     another_code_block
# else:
#     yet_another_code_block

# EXPLANATION : what is a statement
# - any expression that has a result of true or false 
# - for now we know about > and < from math
# - those two operators tell us if a number is greater than or lesser than another number
# - the operation of comparison results in true or false 
# - so it can serve as a statement in the if

# CODE EXAMPLE :
a = 4 
b = 6
if a > b:
    print(a)
else:
    print(b)

# CONCEPT : FORMATING
# EXPLANATION :
# Formating helps us figure out where things end and where other things start in python
#     - you may notice that there are no { } in python, unlike other programming languages
#     - in python we use indentation to replace { }
#     - in c++ for example this is how an if looks

# CODE EXAMPLE C++ :
# if (statement) {
#   // block of code to be executed if statement is true
# } else if (another_statement) {
#   // block of code to be executed if the statement is false and another_statement is true
# } else {
#   // block of code to be executed if the statement is false and another_statement is false
# }

#     - as you can notice the structure is similar
#     - by using { } we don't really care about the indentation of the code inside

# CODE EXAMPLE C++ :
# a = 9
# b = 3
# if (a > b) {
# s = a + b
# d = a - b
# }

# - the statement above is completely valid in c++ and will compile
# - the computer has no problem going through the instructions one by one
# - everything is clear to him

# CODE EXAMPLE PYTHON WITH ERRORS:
# a = 9
# b = 3
# if a > b:
# s = a + b
# d = a - b

# - now if we try to do the same thing in python without paying attention to the indentation
# - like we did above, we may run into a bit of trouble
# - how can the computer know where the if ends
# - how manny of the lines after if should be executed inside the if
# - how manny outside, imagine we have 10 more lines of instructions following the if statement
# - should it take only the first line, only the first 3, the questions never end

# CODE EXAMPLE PYTHON :
a = 9
b = 3
if a > b:
    s = a + b
    d = a - b

# - formatting to the rescue, as you can see above by introducing propper formatting 
# - everything becomes clear
# - what if we don't want everything in the if, no worries just unindent them

# CODE EXAMPLE PYTHON :
a = 9
b = 3
if a > b:
    d = a - b
s = a + b

# - in this example the sum part gets executed every time the program runs
# - not just if a is greater than b like in the previous example

# - if statement (how to check which number is smaller or larger)
# - the <= operator translater to lesser than or equal to 
# - the >= operator means greater than or equal to

# CODE EXAMPLE PYTHON :  
a = 7 
b = 3
if a <= b :
    print(a)
else :
    print(b)
    
# CONCEPT : chained if statements 
# CODE EXAMPLE PYTHON :
a = 8 
b = 4
c = 5
if a > b and a > c :
    print(a)
elif b > a and b > c :
    print(b)
else :
    print(c)

# EXPLANATION : check which number is greater


# CONCEPT : logical operators
# DEFINITION :
#     - A logical operator is like a rule that helps you make a decision. 
#         In Python, there are three main logical operators: and, or, and not.
#     - The and operator helps you make a decision based on two things being true at the same time. 
#         For example, imagine you want to eat ice cream, but only if it's not raining outside. 
#         The rule could be "if it's sunny and you have money, you can have ice cream". 
#         If both things are true, you can have ice cream, but if just one of them is false, 
#         then you can't.
#     - The or operator helps you make a decision based on one of two things being true. 
#         For example, imagine you want to go to the park to play, but you can also play in 
#         your backyard. 
#         The rule could be "if it's sunny, you can go to the park, or if it's not sunny, 
#         you can play in the backyard". If one of these things is true, you can play.
#     - The not operator helps you reverse a decision. For example, imagine you want to go to bed, 
#         but only if it's not too early. The rule could be "if it's not before 8 PM, 
#         you can go to bed". The not operator would change the rule to "if it's before 8 PM, 
#         you cannot go to bed".

#CODE EXAMPLE and :
a = True
b = False
c = a and b
# using symbols will work as well see example below
# c = a & b
print(c)

#CODE EXAMPLE or :
a = True
b = False
c = a or b
# using symbols will work as well see example below
# c = a | b
print(c)

# TABLE OF RESULTS FOR LOGICAL OPERATORS
# A	    B	    A and B	  A or B
# False	False	False	  False
# False	True	False	  True
# True	False	False	  True
# True	True	True	  True

# = vs == 

# "=" is a symbol we use in math and programming to mean "is the same as." 
# For example, if I say "2+2=4," I mean that "2+2" is the same as "4." 
# When we use "=" in programming, we are telling the computer to store a value in a variable. 
# So, if we write "x = 5" in a program, we are telling the computer to store the value "5" 
# in a variable called "x."

# "==" is another symbol we use in programming to mean "is equal to." 
# It's a way to compare two values and see if they are the same. 
# For example, if I write "2+2==5" in a program, the computer will check 
# to see if the value of "2+2" is equal to the value "5." 
# Since they are not the same, the result of this comparison will be "False."

# So, to sum up: "=" is a symbol we use to assign values to variables, 
# while "==" is a symbol we use to check if two values are the same.	

# CODE EXAMPLE :
a = 6 
b = 4
c = a == b
print(c)
c = a > b
print(c)

a = b
c = a == b
print(c)
c = a > b
print(c)

# EXERCISE : 1 
    # - check if a number is even or odd
    # - What operator should be used
    # - Why is that the correct operator
# code section    
a = 8 
if a % 2 == 0 :
    print(True)
else :
    print(False)


# EXERCISE : 2 
    # - check if a number divisible by 5
# code section    
a = 8 
if a % 5 == 0 :
    print(True)
else :
    print(False)


# EXERCISE : 3
    # - given there three variables which represent if the fruit is in storage or not 
    # - create a program that checks which of thee three items are available 
    #     and prints the number of fruits available
# code section    
apples = True
banana = False
coconut = True
nr_of_fruits_available = 0
if apples == True :
    nr_of_fruits_available += 1
#   short for 
#   nr_of_fruits_available = nr_of_fruits_available + 1
if banana == True :
    nr_of_fruits_available += 1
if coconut == True :
    nr_of_fruits_available += 1


# EXERCISE : 4
    # - imagine you are playing rock paper scissors with someone 
    # - now imagine rock paper and scissors are variables containing numbers from 1 to 3
    # - write a program that plays perfectly and defeats the enemy every time
# code section    
# 1 is for rock, 2 for papper, 3 for scissor 
input = 3
if input == 1 :
    # 2 (paper) beats 1 (rock)
    print(2)
if input == 2 :
    # 3 (scissor) beats 2 (rock)
    print(3)
if input == 3 :
    # 1 (rock) beats 3 (scissor)
    print(1)
# change the input and check you can beat the opponent every time


# EXERCISE : 5
    # - given a number between 1 and 24 representing the hour of day 
    # - print 1 if the hour is between 6 and 12 representing the morning
    # - print 2 if the hour is between 12 and 18 representing the afternoon
    # - print 3 if the hour is between 1 to 5 and 19  to 24 representing the night
# code section    
hour = 13
if hour >= 6 and hour <= 12 :
    # morning
    print(1)
elif hour >= 13 and hour <= 18 :
    # afternoon
    print(2)
elif hour >= 1 and hour <= 5 or hour >= 19 and hour <= 24 :
    # night
    print(3)


# EXERCISE : 6
    # - given a number of Lei 
    # - if the number is greater that 50 convert that to euro
    # - if the number is less than or equal to 50 convert that to British pounds
# MENTOR NOTE : 
#     use rounded integer numbers 
#     (good place to start looking things up on google with them)
# code section    
currency = 66
if currency > 50 :
    print(currency*4)
elif currency <= 50 :
    print(currency*5)


# EXERCISE : 7
    # - given a number representing the side of a square
    # - if the rounded division of the number by 4 is 3
    # - print the area and perimeter of the square
# code section    
side = 13
if side // 4 == 3 :
    print(side*4)
    print(side*side)


# EXERCISE : 8
    # - given 4 numbers check which is the greater of them
    # - check with 
# code section    
a = 7
b = 2
c = 4
d = 3
if a > b and a > c and a > d :
    print(a)
elif b > a and b > c and b > d :
    print(b)
elif c > a and c > b and c > d : 
    print(c)
else :
    print(d)


# EXERCISE : 9
    # - given two variables exchange the value of the two using only variable names
    # - if they try to asign numbers directly tell them they can't always rely on knowing the numbers
    # - may want to introduce input function to get the point across (up to each mentor)
# code section     
a = 7
b = 2
c = a
a = b
b = a
print(a)
print(b)


# EXERCISE : 10
    # - imagine you have a budget and you want to buy 4 things
    # - how do you check if you have enough money or not
    # - print true if you have false otherwise
# code section    
budget = 300
a = 159
b = 41
c = 25
d = 75
s = a + b + c + d
if s <= budget :
    print(True)
else :
    print(False)


# EXERCISE : 11
    # - translate the following statement in code and check if it's true or not
    # - 7 is an odd number and 13 is an even number
# code section    
a = 7
b = 13
print(a % 2 == 1 and b % 2 == 0)


# EXERCISE : 12 
    # - given a large number print the second to last digit
# code section    
a = 56898
b = a % 100
b = b / 10
print(b)