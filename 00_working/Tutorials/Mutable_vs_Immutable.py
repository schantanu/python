#%%

# Everything in Python is an Object
# Object consists of a bundle of different types of data and functions logically grouped together
# An object is an instance of a particular class
# A class is a blueprint, and an object is created based on the blueprint

# Below are two examples of list and a function, both are objects of class 'list' and class 'function'

list = [1, 2, 3]
print(type(list))


def square(x):
    x = x * x
    return x


y = square(2)
print(type(square))

# Immutable Objects
# int, float, long, complex, string, tuple, boolean

# Mutable Objects
# list, dict, set, byte array, user-defined classes

#%%

# Checking object id of an immutable object
a = 89
print(id(a))

a = 89 + 1
print(id(a))

# Checking object id of a mutable object
list = [1, 2, 3]
print(id(list))

list.append(4)
print(id(list))

# %%
# Python Memory Management

# In C, when we assign a variable, we first declare it, thereby reserving a space in memory,
# and then store the value in the memory spot allocated. We can create another variable with
# the same value by repeating the process, ending up with two spots in memory, each with its
# own value that is equivalent to the other’s.

# Python employs a different approach. Instead of storing values in the memory space reserved
# by the variable, Python has the variable refer to the value. Similar to pointers in C,
# variables in Python refer to values (or objects) stored somewhere in memory. In fact, all
# variable names in Python are said to be references to the values, some of which are front
# loaded by Python and therefore exist before the name references occur (more on this later).
# Python keeps an internal counter on how many references an object has. Once the counter goes
# to zero — meaning that no reference is made to the object — the garbage collector in Python
# removes the object , thus freeing up the memory.

# http://foobarnbaz.com/2012/07/08/understanding-python-variables/

a = 10
b = 10
c = 10
print(id(a), id(b), id(c))

a += 1
print(id(a), id(b), id(c))

x = 500
y = 500
print(id(x), id(y))

# The current implementation keeps an array of integer objects for all integers between -5 and 256,
# when you create an int in that range you actually just get back a reference to the existing object.
# So it should be possible to change the value of 1. I suspect the behaviour of Python in this case
# is undefined. :-)

# %%
