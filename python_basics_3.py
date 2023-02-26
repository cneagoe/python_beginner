# *****************************************************************************************************
# session 3 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here
#     - lists
#     - list methods : append
#     - list methods : pop
#     - functions : type

# CONCEPT : lists
# EXPLANATION : 
# - Lists in programming are exactly what they are in real life as well
#       an enumeration of elements that we want to save for later.
# CODE EXAMPLE :
# we can have lists of strings :
l = ["apple", "banana", "orange", "blueberries"]
# we can have lists of numbers :
l1 = [3, 4, 8, 1, 7, 2]
# we can have lists of strings and numbers :
l2 = ["apple", 2, "banana", 8]
# How can we access the ellements of a list :
# hold on what is this, we've only used print with one parameter
print(l[0], l[1], l[2])
# no worries we can have as manny parameters in print as we want
# it's called a function with a variable number of arguments
# arguments is just another word for parameters
# we'll talk about this more when we get to functions
# But what does the number inside the brackets represent
# the order of the element in the list

# putting things together
# how to print a list
# we use i as an iterator, this means we use it to iterate through the elements of the list
# every list starts counting its contents from 0, l[0] will always be the first element 
# in the list
l = ["apple", "banana", "orange", "blueberries"]
i = 0
# what we need next is the lenght of the list so that 
# we get this by calling the function len
# len will return to us the length of a list given as parameter
L = len(l)
# now what we have here is an easy short list
print(L)
# lenght will be 4 when we check it
# so this should be pretty easy right
# we can just print each element
print(l[0],l[1],l[2],l[3])
# and there we go, we printed the whole list
# great now do it for a list with 1000000 elements inside of it
# not that easy any more right?
# no worries we can make it easy with while loops
while i < L:
    print(l[i])
    i = i + 1
# looks easy right, just three lines of code and we can print a list as long as we want
# whell how about 100 elements, let's give it a shot
my_list = [23, "abc", 7, "def", 42, "ghi", 12, "jkl", 55, "mno", 18, "pqr", 34, "stu", 91,
    "vwx", 2, "yzs", 8, "abc", 63, "def", 9, "ghi", 1, "jkl", 77, "mno", 29, "pqr", 46, 
    "stu", 13, "vwx", 88, "yzs", 24, "abc", 71, "def",  39, "ghi", 5, "jkl", 68, "mno", 17, 
    "pqr", 52, "stu", 96, "vwx", 31, "yzs", 57, "abc", 84, "def", 22, "ghi", 48, "jkl", 89, 
    "mno", 35, "pqr", 70, "stu", 16, "vwx", 73, "yzs", 30, "abc", 62, "def", 11, "ghi", 95, 
    "jkl", 28, "mno", 53, "pqr", 79, "stu", 43, "vwx", 67, "yzs", 14, "abc", 61, "def", 21, 
    "ghi", 75, "jkl", 38, "mno", 83, "pqr", 44, "stu", 99, "vwx", 50, "yzs", 66, "abc", 25,
    "def", 72, "ghi", 19, "jkl", 60, "mno", 87, "pqr", 36, "stu", 98, "vwx", 45, "yzs"]
i = 0
L = len(my_list)
while i < L:
    print(my_list[i])
    i = i + 1
# works like a charm
# time to put things into practice

# EXERCISE: 1
# write a program that ask the user for input from keyboard until 0 is introduced
# add the elemnts introduced to the list
# print the list
numbers = []
number = 1
i = 0
while number != 0:
    number = int(input("Enter a number, or 0 to quit: "))
    numbers[i] = number
    i += 1
print("The numbers you entered are: ", numbers)

# EXERCISE: 2
# write a program that asks the user to input even numbers untill 0 is introduced
# the program will check if the number is even and will add it to a list
# when the program will end, print the list
even_numbers = []
user_input = 1
i = 0
while user_input != 0:
    user_input = int(input("Enter an even number, or 0 to quit: "))
    if user_input % 2 == 0:
        even_numbers[i] = user_input
        i += 1
print("The even numbers you entered are: ", even_numbers)

# EXERCISE: 3
# NOTE FOR MENTOR : each of the following exercise can be combined with the previous ones 
#                   if you see things are getting too easy
# given the list bellow 
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]
# print all the odd numbers
i = 0
while i < len(my_list):
    if my_list[i] % 2 != 0:
        print(my_list[i])
    i += 1
# what is i += 1
# it's the short form of i = i + 1

# EXERCISE: 4
# given the list below
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]
# Write a program that returns the greatest number in the list
max = 0
i = 0
while i < len(my_list):
    if my_list[i] > max:
        max =  my_list[i]
    i += 1
print("greatest nr is : ", max)

# EXERCISE: 5
# write a program that calculate the average of the numbers in a list
# simpler option with just sum
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]
sum_of_numbers = 0
count_of_numbers = 0
i = 0
while i < len(my_list):
    sum_of_numbers += my_list[i]
    count_of_numbers += 1
average = sum_of_numbers / count_of_numbers
print("The average of the numbers you entered is: ", average)

# EXERCISE: 6
# Write a program that takes a list of numbers 
# and returns a new list that contains the numbers in reverse order.
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]
reverse_list = []
i = len(my_list)-1
j = 0
while i >= 0:
    reverse_list[j] = my_list[i]
    # short form for i = i - 1
    i -= i
print(reverse_list)

# python is a very nice language and it offers us a lot help when it comes to lists
# CONCEPT : list methods : append
# EXPLANATION : 
# - adds items to a list
# CODE EXAMPLE :
numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(3)
print(numbers)

# EXERCISE: 7
# Write a program that asks for names from the user until he inputs "stop"
names = []
user_input = ""
while user_input != "stop":
    user_input = input("Enter a name, or 'stop' to quit: ")
    if user_input == "stop":
        break
    names.append(user_input)
print("The names you entered are: ", names)

# CONCEPT : list methods : pop
# EXPLANATION : 
# - removes items from the list that are found at a particular index 
# CODE EXAMPLE :
my_list = [1, 2, 3, 4, 5, 6]
my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)

# EXERCISE: 8
# remove all numbers from the list that are dividible by 3
# NOTE FOR MENTOR : carefull with this one they will most like miss the decrement
#                   and end up with a list containing 6 
#                   worth to spend some time to debug, add print i and print my_list[i]
#                   and go through with them step by step
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20]
i = 0
while i < len(my_list):
    if my_list[i] % 3 == 0:
        print(my_list[i])
        my_list.pop(i)
        i -= 1
    i += 1
print(my_list)

# EXERCISE: 9
# Write a program that asks the user to enter a positive integer and then 
# prints whether the number is prime or not.
# if it's prime add it to a list 
# print the list at the end
num = int(input("Enter a positive integer: "))
count = 2

while count < num:
    if num % count == 0:
        print("The number is not prime.")
        break
    count += 1
else:
    print("The number is prime.")

# EXERCISE: 10
# Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = []
i = 0
while i < len(a)-1:
    j = i+1
    while j < len(a):
        if a[i] == a[j]:
            dup_items.append(a[i])
        j += 1
    i += 1
print(dup_items)

# EXERCISE : 11
# Write a Python program to convert a list of characters into a string
char_list = ['h', 'e', 'l', 'l', 'o']
str = ""
i = 0
while i < len(char_list):
    str += char_list[i]
    i += 1
print(str)

# CONCEPT : type function 
# EXPLANATION : returns the type of the object
x = 5
s = "geeksforgeeks"
y = [1, 2, 3]
print(type(x))
print(type(s))
print(type(y))

# EXERCISE : 12
# Given a list containing both numbers an letters
# Create two new lists, one only containing numbers and one letters 
l = ['h', 50, 'e', 46, 29, 'l', 8, 53, 91, 7, 'l', 'o']
i = 0
nr = []
ltr = []
while i < len(l):
    if type(l[i]) == int :
        nr.append(l[i])
    if type(l[i]) == str :
        ltr.append(l[i])
    i += 1
print(nr)
print(ltr)
