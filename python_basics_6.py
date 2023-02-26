# *****************************************************************************************************
# session 6 (around 1 hour 30 min depending on mentor availability)
# -----------------------------------------------------------------------------------------------------
# MENTOR NOTE : 
# stuff covered here
#     - for loops

# CONCEPT : for loop
# EXPLANATION : A for loop in Python is a way to repeat a set of instructions multiple times. 
# Imagine you have a list of items and you want to do the same thing with each item. 
# Instead of writing the same code over and over again for each item, you can use a for loop.
# We have been using while loops to get you more acustomed to the way lists and strings work.
# Usually while is used when we are dealing with an unknown number of elements.
# We use for when the number of elements is known. 
# GENERAL SYNTAX :
# for <variable> in <collection>:
#     <block>
# EXAMPLE :
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print("I like to eat " + fruit)

# EXERCISE 1 :
# Write a function that takes a string and returns the number of times each letter appears in the string
def nr_of_times(word):
    for letter in word :
        nr = 0  
        for l in word :
            if letter == l :
                nr += 1
        print("letter " + letter + " appears " + str(nr) + " times")
word = "supercalifragilisticexpialidocious"
nr_of_times(word)

# CONCEPT : range function
# Explanation : is used to generate a sequence of numbers and to create lists or other sequences of numbers.
# with one parameter it generates numbers from 0 to n-1
# EXAMPLE :
for i in range(5):
    print(i)
# with two parameters it generates numbers from the first number given to the seccond -1
# EXAMPLE :
for i in range(3, 7):
    print(i) 
# with three parameters it specifies also the size of the step taken with each increment
# EXAMPLE :
for i in range(1, 9, 2):
    print(i)


# EXERCISE 2 : 
# optimize the previous exercise so that in the seccond loop you start from the 
# current letter you are on not the begining of the word
def nr_of_times(word):
    for i in range(0,len(word)) :
        nr = 0  
        for j in range(i, len(word)) :
            if word[i] == word[j] :
                nr += 1
        print("letter " + word[i] + " appears " + str(nr) + " times")
word = "supercalifragilisticexpialidocious"
nr_of_times(word)

# CONCEPT : in / not in 
# EXPLANATION : in and not in are special words in computer programming 
# that we use to check if something is inside or outside of something else.
# EXAMPLE :
basket = ["apple", "banana", "grapes"]
if "apple" in basket:
    print("There's an apple in the basket!")

# EXERCIES 3 : 
# given a list of years of birth create a function that returns a list with the current age  
def age(years_of_birth):
    ages = []
    for year in years_of_birth: 
        ages.append(2023 - year)
    return ages
years_of_birth = [1990, 1991, 1989, 1996, 1992, 1999]
print(age(years_of_birth))

# CONCEPT : method insert
# EXPLANATION : 
# adds an item to a list at a specific position, shifting the rest of the items to the right.
# EXAMPLE :
fruits = ["apple", "banana", "grapes"]
fruits.insert(1, "orange")
print(fruits)

# EXERCISE 4 :
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.
def reverse(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)
x = "This is a brand new sentence."
print(reverse(x))

# CONCEPT : slices
# syntax works very similarly to the range function, which means we can also give it a step:
my_string = "exemplary"
print(my_string[0:7:2])
my_list = [1,2,3,4,5,6,7,8]
print(my_list[6:2:-1])

# EXERCISE 5 :
# Please write a function named everything_reversed, which takes a list of strings as its argument. 
# The function returns a new list with all of the items on the original list reversed. 
# Also the order of items should be reversed on the new list.
def everything_reversed(strings):
    reversed_strings = []
    for string in strings:
        reversed_strings.append(string[::-1])
    return reversed_strings[::-1]
strings = ["hello", "world", "this", "is", "a", "test"]
print(everything_reversed(strings))

# EXERCISE 6 :
# Please write a function named count_matching_elements(my_matrix: list, element: int), 
# which takes a two-dimensional array of integers and a single integer value as its arguments. 
# The function then counts how many elements within the matrix match the argument value.
def count_matching_elements(my_matrix, element):
    count = 0
    for row in my_matrix:
        for num in row:
            if num == element:
                count += 1
    return count
my_matrix = [[1, 2, 5], [4, 5, 6], [7, 8, 9]]
element = 5
print(count_matching_elements(my_matrix, element))