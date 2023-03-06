# *****************************************************************************************************
# session 5 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here
#     - functions
#     - parameters
#     - statement : return

# CONCEPT : functions
# EXPLANATION : We have already used functions such as len, print and input in our programs. 
# These are functions built into Python, and so they are always ready at our disposal, 
# no matter which environment we are programming in. However, 
# it is also possible to define your own functions.
# EXAMPLE :
def message():
    print("This is my very own function!")
message()

# CONCEPT : parameters
# EXPLANATION : Functions often take one or more parameters, 
# which may affect what the function does. For example, 
# the built-in Python functions print and input 
# take as argument(s) the text that is to be displayed:
print("Hi!")                           # argument is the string "Hi!"
name = input("What is your name? ")    # argument is the string "What is your name? "
print(name)                            # argument is the value of the variable name

# EXERCISE : 1
# Create a function that returns the first letter of a word
def first_character(text):
    print(text[0])
# TEST :
first_character('python')
first_character('yellow')

# EXERCISE : 2
# Create a function that takes three parameters 
# and returns the mean of these three elements.
def mean(a, b, c) :
    print((a + b + c)/3)
# TEST :
mean(5, 3, 1)
mean(10, 1, 1)

# EXERCISE : 3
# write a function named print_many_times(text, times), 
# which takes a string and an integer as arguments. 
# The integer argument specifies how many times the string argument should be printed out:
def print_many_times(tx, tm) :
    i = 0
    while i < tm :
        print(tx)
        i += 1
# TEST :
text = "All Pythons, except one, grow up"
times = 3
print_many_times(text, times)

# EXERCISE : 4
# write a function named hash_square(length), which takes an integer argument. 
# The function prints out a square of hash characters, 
# and the argument specifies the length of the side of the square.
def hash_square(a) :
    i = 0
    while i < a :
        print("#"*a)
        i += 1
# TESTS : 
hash_square(3)
hash_square(6)

# EXERCISE : 5
# write a function named chessboard, which prints out a chessboard made out of ones and zeroes. 
# The function takes an integer argument, which specifies the length of the side of the board.
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1
# TEST :
chessboard(3)
chessboard(6)

# CONCEPT : Return statement
# EXPLANATION : Functions can also return values. 
# For instance, the built-in Python function input 
# returns an input string typed in by the user. 
# The value returned by a function can be stored in a variable
# EXAMPLE :
word = input("Please type in a word: ")

# EXERCISE : 6
# Create a function that asks the user to input a number,
# converts the string to int and return the int
# the fuction should be called get_input_number
def get_input_number():
    return int(input("Enter a number: "))

# EXERCISE : 7
# Create a function that uses the function from  
# exercise 6 to ask the user for a number untill
# he introduces a negative one,
# the numbers will be saved in a list and returned
def get_numbers_list():
    l = []
    a = get_input_number()
    while a > 0:
        l.append(a)
        a = get_input_number()
    return l

# EXERCISE : 8
# Create a function that calculates and returns the max from a list
# the function should be called get_max()
def get_max(l):
    i = 0
    max = 0
    while i<len(l):
        if l[i] > max :
            max = l[i]
        i += 1
    return max

# EXERCISE : 9
# Create a function that uses the function from  
# exercise 8 to find the biggest number and return the indexes 
# where it's found in the list
# function should be called get_idx_max
def get_idx_max(max, l):
    i = 0
    idx = []
    while i < len(l):
        if l[i] == max:
            idx.append(i)
        i += 1
    return idx

# EXERCISE : 10
# Create a function that takes two lists as parameters
# the first parameter is the list introduced by the user
# the seccond one is the list of indexes where the max can be found
# return the numbers righ before and after each max in the list
# if there are no numbers before or after it it should return 0
# function should be called get_pre_post
def get_pre_post(lu, lm):
    i = 0
    r = []
    while i < len(lm):
        if lm[i] == 0 :
            r.append(0)
            r.append(lu[0])
        elif lm[i] == len(lu)-1 :
            r.append(lu[len(lu)-2])
            r.append(0)
        else :
            r.append(lu[lm[i]-1])
            r.append(lu[lm[i]+1])
        i += 1
    return r

# EXERCISE : 11
# Creates a script that, using all the functions created previously 
# ansk the user to insert a list, find the greates number in that list and
# return a list containing the numbers before and after the max each time 
# it's found in the string
l = get_numbers_list()
x = get_max(l)
i = get_idx_max(x, l)
y = get_pre_post(l, i)
print(y)

# EXERCISE 12
# Rewrite the previous exercise without the use of functions

l = []
a = int(input("Enter a number: "))
while a > 0:
    l.append(a)
    a = int(input("Enter a number: "))
i = 0
max = 0
while i<len(l):
    if l[i] > max :
        max = l[i]
    i += 1
i = 0
idx = []
while i < len(l):
    if l[i] == max:
        idx.append(i)
    i += 1
i = 0
r = []
while i < len(idx):
    if idx[i] == 0 :
        r.append(0)
        r.append(l[0])
    elif idx[i] == len(l)-1 :
        r.append(l[len(l)-2])
        r.append(0)
    else :
        r.append(l[idx[i]-1])
        r.append(l[idx[i]+1])
    i += 1
print(r)

# as you can observe doing it all in one go
# is not the best way to aproach complex problems
# tracking down manny lines of code without functions 
# is demanding on our working memmory 
# having functions also allows us to reuse code 
# in future implementations of similar problems 