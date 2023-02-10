# General notes
# in Spyder, default for running selection or line was F9, I swapped run cell (default: Ctrl+Enter) with it. Now it works like R
# to move between editor and console use ctrl+shift+I and ctrl+shift+E
# #%% creates a new cell

#%% - Importing Libraries
import numpy as np ; 
import pandas as pd
import math

#%%
# Some general basic functions
type(4)                                                                         # type function shows the type of an object
n = [1, 3, 6, 8, 13, 1, 4]
sum(n)                                                                          # sum of the numbers in the list
len(n)                                                                          # length of the list
k = ([True, 6 == 5, 4 > 3, None is None, 7, round(math.pi, 4)]) 
del n                                                                           # to delete a variable
sum(k)/len(k)                                                                   # there are 3 true values and a 7 totalling 10 divided by 5 gets 2 (as float)
[None]*5                                                                        # to create a list containing 5 None items
type(None)
k.sort()                                                                        # to sort the items inside a list
np.mean(k)

#%%
a = np.array([0,1,2,3,4,5,6,7,8,9,10])
np.mean(a)
url = "https://raw.githubusercontent.com/curran/data/gh-pages/Rdatasets/csv/COUNT/nuts.csv"
df = pd.read_csv(url) ; type(df)
df.head(3)                                                                      # see the top 3 rows of data 
df.columns                                                                      # to see the name of the variables / columns

#%% LOC and iLOC
# .loc uses labels/column names to call the data from the dataframe
df = df.loc[:, ["cones", "ntrees", "dbh", "height", "cover", "sntrees", "sheight", "scover"]] # removed the index column
df.columns                                                                      # to see the name of the variables / columns
df.loc[:,"ntrees"].head(4)
df.loc[:, ["cones", "ntrees", "dbh", "height", "cover", "sntrees", "sheight", "scover"]].tail(6) # removed the index column
df.loc[:10, ["cones", "ntrees", "cover", "height"]]                             # show 10 observation for these columns in order that is written
df.loc[5:10,]                                                                   # sepefic rows for all columns

# .iloc uses integer numbers to slice the dataframe
df.iloc[:4]                                                                     # first 4 rows of the dataframe
df.iloc[1:5, 2:4]                                                               # rows 1 to 5 (exclusive) and columns 2 to 4 (exclusive on the 4) - note, index starts from 0

df.cones.unique()                                                               # to get the unique values in a column of a dataframe
df.groupby(["cones", "ntrees"]).size()                                          # to group by the combination of two or more variables and show a sumamrization value (size(count), mean, etc.)

#%% Functions
# an example of creating a function
def biglittle():
    text_with_no_space = input("write some text without spaces:")
    funny = max(text_with_no_space) + " " + min(text_with_no_space)
    return funny

biglittle()

# another example of a function
def greet(lang): # the function receives one input, simply labeled lang here and does work with it and returns something 
    if lang == "es":
        print("Hola!")
    elif lang == "fr":
        print("Bonjour!")
    else:
        print("Hello!")

greet("fr") # sends the first parameter into the function

def greet(lang): # same function as above but this time it returns a value instead of printing
    if lang == "es":
        return "Hola!"
    elif lang == "fr":
        return "Bonjour!"
    else:
        return "Hello!"
print(greet("es"), "Jean-claude")

# another example of a function: can receive more than one parameter, label them as they come in, work with them and return 
def addtwo(x, boo):
    added = x + boo
    return added                                                                # return usually is the last line in a fucntion
print(addtwo(6, 90))

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("the sum is equal to: ", addtwo(a,b))
except:
    print("Can't do that! Please enter numbers only")

#%% While Loop: aka indefinite loops but mostly we use definite loops
n = 5                                                                           # this is the iteration variable - will need to change or otherwise the loop goes forever
while n > 0:
    print(n)
    n -= 1
print("It's Over")

# another example
n = 0
while True:
    line = input("Say my name: ")
    if line == "Done":
        break
    print(line)
print("Finally it's over!")

#%% For Loop
n = list(range(1,6))                                                            # just defining a list of numbers to work with in the For loop
for x in n:
    print(x)

guys = ['ali', 'hasan', 'haji']
for name in guys:
    print("Happy new year, ", name)

#%% Data Types
a = 'abc&xyz'           # string
b = 3.16                # float
c = {2:'a', 3:'b'}      # dictionary
d = 6 < 2               # boolean
e = [1,2,3,4,5]         # list
f = sum(e)              # value returned from a function (integer in this case)
g = sum                 # a function

for obj in [a,b,c,d,e,f,g]:
    print(obj, "is of type", type(obj))

#%% Lists
"""
To Distinguish between list, tuple, and dictionary:
    If there is a sequence separated by commas standing alone, it is a tuple.
    If surrounded by parentheses, still a tuple.
    If surrounded by brackets, it a list.
    If surrounded by “curly braces”, it is a set/dictionary.
"""
x = []                                                                          # to create an empty list in an implicit way
x = list()                                                                      # to create an empty list in an explicit way
x = [1, 20, 2, 2, True, 3, False, 5, "hi"]                                                   # a list can contain anything
print(x[1])                                                                     # to see the item on index 1 (indices on lists start from 0)
print(x[2:6])                                                                   # to see the items on index 2 to 5 (last number exclusive)
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]               # 2D list is a good structure for representing grids
myclass = [
        ["Kenny", "American", 9],
        ["Tanya", "Ukrainian", 9],
        ["Madison", "Indian", 7]
        ]
print(heights[2][1])                                                            # to call an item in a 2D list we use two [], first to call the list index, second to call the item index in the list
print(myclass[1])                                                               # print the whole list in the 2D list called by its index
print(myclass[-2][-2])

# different ways to update or extract info from a list
x.append([True])                                                                # Appends the item to the end of the list, whatever the item is!
x.append(True)
x[1:2]=["Two", "three"]
x += [23, "No", False]

# [None] is an list with 1 Null or No-value itemNone is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
x.append([None]*5)
x.append(2)
x.remove(2)                                                                     # removes the item from the list the first time it shows up in the list (for removing by index, use pop() method)
x = x[0:5]
x.extend([6, "Yes", False])                                                     # to append more than 1 item, we extend: equivalent to concatenating two lists
myclass[1][1] = "Albanian"                                                      # same index as [-2][-2]
print(myclass[-2][-2])
myclass[1].remove("Tanya")                                                      # to remove or append an item from/to a list inside a 2D list, apply the function on the specific list inside!
myclass.sort()                                                                  # to sort the list (based on the first elements of each list inside a 2D list)

x.insert(0, 3)                                                                  # to insert a new entry into a list using index: .insert(index, value)
x.insert(-4, "text this time")
x.pop(1)                                                                        # to remove an antery from a list using index: .pop(index) - without an index it simply removes the last one
r=x.pop(1)                                                                      # we can save the removed value to a variable if we care to use it later
print(r)
print(x)

y = range(10)                                                                   # range(start, end/exclusive, step) is unique in that it creates a range object! 
print(y)
print(list(y))                                                                  # to use a range object as a list, we have to convert it using the list() function
z = list(range(2, 20, 2)) 
len(z)                                                                          # to see the length of a list
z[8:6]                                                                          # to show a slice of the list
z[:5]                                                                           # from index 0 to 5 (exclusive) aka first 5 items
z[-2:]                                                                          # last two values in the list
x.extend([3, 4,5, 3,2, 3])
x.count(3)                                                                      # how many of the specified item exist in the list
c = heights.count(["Ava", 70])
print(c)

name = list("GISHAR!")
print("name = ", name)                                                          # this is what list function does to strings.
name.sort()                                                                     # this is a method to sort the original list. after this is done, if you print the list, you'll see the sorted version
print("soreted name = ", name)
name.sort(reverse=True)
print("reverse sorted name = ", name)

sortedname = sorted(name, reverse = False)                                      # this is function to create a sorted version of the original list
print("sorted name = ", sortedname)

examples = ['red', 'green', 'blue', 'orange']
for color in range(len(examples)):
    print(examples[color])

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)                                         # zip() takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs.
print(names_and_heights)                                                        # a zip object - to see what's inside use list() function
print(list(names_and_heights))

#%% Tuples
mytuple = ('Mike', 24, 'Programmer')
mytuple[0]
mytuple[1:]                                                                     # all the same like those in list but nothing can change with tuples
name, age, occupation = mytuple                                                 # unpacking a tuple by putting variables equal to tuple (no of vars equal to no of elements in tuple - order matters)
x = (4,)                                                                        # to create a one element tuple we need the , in there. Otherwise, it's just a number and not a tuple

#%%
