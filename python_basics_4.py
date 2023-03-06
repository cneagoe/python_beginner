# *****************************************************************************************************
# session 4 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here
#     - strings
#     - concatenation
#     - indexes
#     - slices
#     - multiplication
#     - method : find
#     - statement : break

# CONCEPT : Strings
# EXPLANATION : Strings are a type of data in computer programming. 
# Imagine they're like a collection of letters and numbers 
# that make up a word or a sentence. 
# In Python, we use quotation marks or single quotes
# to mark the beginning and end of a string.
# CODE EXAMPLE :
a = "Hello"
print(a)
b = 'Hello'
print(b)

# CONCEPT : Strings concatenation
# EXPLANATION : We can stich strings together using the addition operator.
# CODE EXAMPLE :
a = "Hello"
b = "World"
c = a + b
print(c)

# EXERCISE 1
# Write a program which prints out a line of hash characters, 
# the width of which is chosen by the user.
x = int(input("Width: "))
j = 1
s = ""
while j <= x : 
    s += "#"
    j += 1
print(s)

# EXERCISE 2
# Write a program which prints out a rectangle of hash characters, 
# the width and height of which is chosen by the user.
w = int(input("Width: "))
h = int(input("Height: "))
j = 1
while j <= h : 
    i = 1
    s = ""
    while i <= w :
        s += "#"
        i += 1
    j += 1
    print(s)

# CONCEPT : Acessing string elements
# EXPLANATION : We can use the same way we work with lists 
#               to access the individual elements of the list,
#               We can use negative numbers to parse the list
#               in reverse order.
# CODE EXAMPLE : 
a = "Hello World"
l = len(a)
i = 0
while i < l :
    print(a[i])
    print(a[-i])
    i += 1

# EXERCISE 3
# Write a program which asks the user for a string. 
# The program then prints out a message based on whether 
# the second character and the second to last character 
# are the same or not.
x = input("Please type in a string: ")
if x[1] == x[len(x)-2] :
    print(f"The second and the second to last characters are ", x[1])
else : 
    print("The second and the second to last characters are different")

# CONCEPT : String slices
# EXPLANATION : We can take a slice out of a string this way
# CODE EXAMPLE : 
a = "Hello there"
b = a[:4]
c = a[5:]
d = a[3:7]
print(b)
print(c)
print(d)

# EXERCISE 4 :
# Calculate the length of a string (same thing the len function does)
string = "Hello, World!"
length = 0
for char in string:
  length += 1
print(length)

# EXERCISE 5 :
# Write a program that counts the number of vowels in a string.
string = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0
for char in string:
  if char in vowels:
    count += 1
print(count)

# EXERCISES 6 :
# Write a program that reverses a string.
string = "Hello, World!"
reversed = ""
i = len(string) - 1
while i >= 0:
  reversed += string[i]
  i -= 1
print(reversed)

# EXERCISE 7 :
# Write a program that checks if a word is a palindrome 
# (a word that reads the same forwards and backwards).
word = "racecar"
is_palindrome = True
for i in range(len(word) // 2):
  if word[i] != word[-i - 1]:
    is_palindrome = False
    break
print(is_palindrome)

# CONCEPT : string multiplication
# EXPLANATION : python offers us a verry simple way 
#               to print the same string multiple times
# CODE EXAMPLE :
# no shortcut
i = 0 
while i < 5 :
    print("my string")
    i += 1
# CODE EXAMPLE : 
# with shortcut
print("my string \n"*5)
# the \n is nothing special, it's just the new line character
# so that we can get the same result as the previous chunk of code

# EXERCISE : 8
# Write a program which asks the user for strings using a loop. 
# The program prints out each string underlined as shown in the examples below. 
# The execution ends when the user inputs an empty string - 
# that is, just presses Enter at the prompt.
s = "-"
while s != "" :
    s = input("Please type in a string: ")
    l = len(s)
    p = "-"*l
    print(s)
    print(p)

# EXERCISE : 9
# write a program which asks the user for a string and then prints it out 
# so that exactly 20 characters are displayed. 
# If the input is shorter than 20 characters, 
# the beginning of the line is filled in with * characters.
y = input("Please type in a string: ")
i = 20 - len(y)
s = ""
while i > 0 :
    s += "*"
    i -= 1
print(s+y)

# EXERCISE : 10
# print a piramid the size of 5 letters at the base
# with the letter a ussing string multiplication
i = 1
nr_of_spaces = 3
while i < 6:
    print(" "*nr_of_spaces, "a"*i)
    i += 2
    nr_of_spaces -= 1
# OUTPUT :
#     a
#    aaa
#   aaaaa

# CONCEPT : the find method 
# EXPLANATION : takes the substring searched for as an argument, 
# and returns either the first index where it is found, 
# or -1 if the substring is not found within the string.
# EXAMPLE:
input_string = "test"
print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))

# EXERCISE : 11
# Given the word perpendicular, let the user introduce strings until 
# no string is entered (enter is pressed) then search for these strings 
# inside the word, print the index the substring is found at
input_string = "perpendicular"
while substring != "" :
    substring = input("What are you looking for? ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")

# CONCEPT : break
# EXPLANATION : break out of a look
# EXAMPLE :
i = 0 
while True:
   if i == 5:
      break
   i += 1

# EXERCISE : 12
# Write a program which prints out all the substrings which are 
# at least three characters long, and which begin with the character specified by the user
# SAMPLE INPUT/OUTPUT :
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot
x = input("Please type in a word: ")
y = input("Please type in a character: ")
while len(x) >= 3:
    # print("x " + x)
    i = x.find(y)
    if i < 0 :
        break
    elif len(x[i:i+3]) >= 3 :
        print(x[i:i+3])
        x = x[i+1:]
    else :
        break