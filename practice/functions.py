# Functions:
# -----------

# The block of statements are used to perform the functional operation is known as Method/ Function.
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. 
# A function can return data as a result.

# User Defined Functions:
# ------------------------

''' The function created by the developer are known as userdefined function. These functions are divided into two types 
    They are 1) called functions( contains functional logical statements )
             2) calling functions '''

# 1) called functions:
# --------------------

# The functions which hold the logical statements which are used to perform specific functionality is known as called functions.
# Use the 'def' keyword to create called function.
''' The called function contains the other components like function name followed by parenthesis, set of parameters, set of statements, 
    and return optional.
    syntax:
           def function_name(p1, p2, .....):
           	    statement1
           	    statement2
           	    ..........
           	    return somedata '''

# 2) calling function:
# --------------------

# It is reference of called function used to execute the called statements.
# calling function contains the function name and set of values to the parameters.

# Note:  No called function will gets execution without calling function.
'''syntax:
          function_name(value1, value2, .........)'''


def add(a, b):
	return a + b
print(add(10, -10))

# Default parameters:
# -------------------

# Default parameters are used to increase the function accessability.
# To create a default parameter use variable assignment process is called function signature.

def add(a, b = 10, c = 0):
	return a + b + c
print(add(10))
print(add(10, 0, 8))
print(add(10, 8, 8))

def add(a, b, c = 0):
	return a + b + c
print(add(10, 10))
print(add(10, 0, 8))
print(add(10, 8, 8))

def my_function():
  print("Hello from a function")

my_function()

# Arbitary parameters/ Arbitary arguments:(*args, **kwargs)
# -------------------------------------------------

# The parameter which allows the user to access unknown number of parameters are known as Arbitary parameters.

# *args: (* ---> tuple i.e. (),  args ----> variables)
# -----------------------------------------------------

# args will allows unknown number of elements(parameters) given by user.or

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name 
# in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:
# The element given by user gets stored in a tuple format.

'''Parameters or Arguments?
   The terms parameter and argument can be used for the same thing: information that are passed into a function.

   From a function's perspective:

   A parameter is the variable listed inside the parentheses in the function definition.

   An argument is the value that is sent to the function when it is called.'''


''' Number of Arguments
    By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, 
    you have to call the function with 2 arguments, not more, and not less.'''


# Example
# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Ravi", "Teja")



def test(*a):
    return (a)
print(test())
print(test(10))
print(test(10,20,20))


def test(a, b = 0, *c):
    return (a, b, c)
print(test(10))
print(test(10, 20))
print(test(0, 15, 20, 40))

def name(*kids):
    print("The youngest child is " + kids[1])
name("Sahi", "Neeha")


# **kwargs: (** ----> dictioary i.e. {},   k is key and w is  word(value) args is item)
# --------------------------------------------------------------------------------------

# This is an arbitary parameter which allows the user to access unknown number of items.
# To pass an item use variablle assignment process is called function signature.


def test(**a):
    return a
print(test())
print(test(k = 0))
print(test(b = 0, c = 1))

def test(a, b = 0, *c, **d):
    return a, b, c, d
print(test(10))
print(test(10, 20, 25, 40, 50, 60, k = 60, m =  10, n = 25))

'''note: while working with multiple parameters combintion follow the order i.e. mandatory parameters ----> default parameters
        ------> * args -----> **kwargs 
        the order of placing the parameter is i.e. mandatory parameters ---> default parameters ---> *args ---> **kwargs'''


d = {'a': 1, 'b': 2}
def get_value(key):
    if key in d:
        return d[key]
    else:
        return 'No key is available'
print(get_value('b'))
print(get_value('x'))

def get_value(key, value = 100):
    if key in d:
        return d[key]
    else:
        return value
print(get_value('b'))


def add(a, b = 10, *c, **d):
    return a + b + sum(c) + sum(d.values())
print(add(10, 20, 25, 98, m = 10, n = 25))
print(get_value('x'))
print(get_value('y', 100))


def add(a, b):
    print(a+b)
add(10, 20)
add(10, -10)

def get_name(fname):
    print(fname+" reddy")
get_name('teja')


def name(**key):
    print("The first name is "+key['fname']+" The last name is "+key['lname'])
name(fname='Neeha', lname='Reddy')

def country(name='local'):
    return name
print("I am " + country())
print("I am from "+country('India'))


def my_function(food):
    for i in food:
        print(i)
fruits = ['apple','mango']
my_function(fruits)


# The pass Statement:
# --------------------

''' function definitions cannot be empty, but if you for some reason have a function definition with no content, 
    put in the pass statement to avoid getting an error.'''

# Example
def myfunction():
  pass



'''Recursion:
     Python also accepts function recursion, which means a defined function can call itself.

     Recursion is a common mathematical and programming concept. It means that a function calls itself. 

     This has the benefit of meaning that you can loop through data to reach a result.

     The developer should be very careful with recursion as it can be quite easy to slip into writing 
     a function which never terminates, or one that uses excess amounts of memory or processor power. However, 
     when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

     In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
     We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends
     when the condition is not greater than 0 (i.e. when it is 0).

     To a new developer it can take some time to work out how exactly this works, 
     best way to find out is by testing and modifying it.'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



# functional programming tools:
# -----------------------------

# These tools are reduce the complexity and memory consumption of itterable blocks[for, while, etc].
# Python supports four types of functional programing tools. they are 1)filter(), 2)map(), 3)reduce(), 4)zip()

# 1) filter():
# ------------

# This method is used to perform filtering operations on given data_structure.
# filter method takes exactly two parameters. they are function_name, and dta_structure.
# The output format always < filter object >

# Note:
# filter will collect one element from given data_structure and invokes (calls/executes) the given function_name.
# The result of specific function will inserted into filter object.
# This method will repeats till all the elements are processed.

'''syntax:
          def function_name(p1):
             ------------------
             ------------------
             return 'soedata'
          filter(function_name, data_structure)'''

def even(a):
    if a % 2 == 0:
        return a
print(filter(even, [1, 2, 3, 4, 5, 6, 7, 8]))
print(list(filter(even, [1, 2, 3, 4, 5, 6, 7, 8])))


# 2) map():
# ---------

# This method is used to perform manipulation opertion on the elements of given data_structure individually.
# map method takes exactly two parameters like filter.
# The output format is always < map object >

'''syntax:
         def function_name(p1):
            ------------------
            ------------------
            return
         map(function_name, dta_structure)'''

def square(a):
    return a * a
print(map(square, [1, 2, 3, 4]))
print(list(map(square, [1, 2, 3, 4])))


# 3) reduce():
# -------------

# This method is used to perform the manipulation operation in between the elements of given data_structure.
''' The syntax is similar to filter and map. but, unlike filter and map reduce method takes two elements 
    from given data_structure. and invokes the given function.'''
# The output will be return to calling function once after processing all the elements.

''' syntax:
           def function_name(p1, p2):
               ----------------------
               return 'somedata'
           reduce(function_name, data_structure)'''


from functools import reduce
l = [1, 2, 3, 4]

def add(a, b):
    print(a, b, a + b)
    return a + b
print(reduce(add, l))


# 4) zip():
# ----------

# This method is used to combine the elements of given data_structure based on the position elements.
# This method takes any number of parameters(atleast two parameters).
# The output format is always a zip object.
'''syntax:
          zip(data_structure1, data_structure2, ......)'''

l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 7]
print(zip(l1,l2))
print(list(zip(l1,l2)))

print(list(zip('Hello', [1, 2, 3, 4], (5, 6, 7), {'a': 8, 'b': 9})))

# assign function to a variable
x = 123
def display():
    x = 678
    print(x)
    print(globals()['x'])
print(x)
display()
display()


# function inside another function
def display(name):
    def message():
        return 'hello '
    result = message() + name
    return result
print(display('bharath'))


# function as parameter to an other
def display(fun):
    return "hello " + fun
def name():
    return "RaviTeja"
print(display(name()))


# returning functions

'''def display():
    def message():
        return 'hello'
        return message
fun = display()
print(fun())'''


# pass and type
def fun(lst):
    for i in lst:
        print(i)
fun([1, 2, 3, 4])

# recursion
# recursion is the process of function calling it self

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    return result
print(factorial(5))


def average(a = 10, b = 20):
    print(a)
    print(b)
    return (a + b)/2
print(average())
print(average(a = 30))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))






