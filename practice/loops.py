# General Structure of a Loop:
# ---------------------------

''' Many algorithms make it necessary for a programming language 
    to have a construction which makes it possible to carry out a sequence of statements repeatedly.
    The code within the loop, i.e. the code carried out repeatedly, is called the body of the loop.

    Essentially, there are three different kinds of loops:
    Count-controlled loops: A construction for repeating a loop a certain number of times. 
                            An example of this kind of loop is the for-loop of the programming language C:

                            for (i=0; i <= n; i++)

                            Python doesn't have this kind of loop.

    Condition-controlled loop: A loop will be repeated until a given condition changes, 
                               i.e. changes from True to False or from False to True, depending on the kind of loop.
                               There are 'while loops' and 'do while' loops with this behaviour.

    Collection-controlled loop: This is a special construct which allows looping through the elements of a 'collection', 
                                which can be an array, list or other ordered sequence. Like the for loop of 
                                the bash shell (e.g. for i in *, do echo $i; done) or the foreach loop of Perl.'''

'''Python supplies two different kinds of loops: the while loop and the for loop, 
   which correspond to the condition-controlled loop and collection-controlled loop.'''

'''Most loops contain a counter or more generally, variables, which change their values in the course of calculation.
   These variables have to be initialized before the loop is started. 
   The counter or other variables, which can be altered in the body of the loop, 
   are contained in the condition. Before the body of the loop is executed, the condition is evaluated. 
   If it evaluates to False, the while loop is finished. In other words, 
   the program flow will continue with the first statement after the while statement, 
   i.e. on the same indentation level as the while loop. If the condition is evaluated to True, 
   the body, - the indented block below the line with "while" - gets executed. 
   After the body is finished, the condition will be evaluated again. 
   The body of the loop will be executed as long as the condition yields True.'''

# Iterable Control Statements:
# ----------------------------

# This statement which are used to excute a set of instructions repeatdely are known as Iterable control statements.
''' Python supports two types of control statements. They are
     1) while loop(conditional-controlled loop)
     2) for loop(collection-controlled loop)'''


# 1) while loop:
# --------------

# With the while loop we can execute a set of statements as long as a condition is true.or 
# while is used to create and itterable block which executes set of staments repeatdely.
# unlike for loop while loop requires the variable assignment, condition and increaments/decreaments operation
# The scope of while loop using very less because it may creates an infinite loop 
''' syntx:
           variable_name = value
           while conditon:
           	    statement1
           	    statement2
           	    ----------
           	    increament/decreament
           	out of block'''


# eg:Print i as long as i is less than 6:

i = 1
while i < 6:
	print(i)
	i += 1      # 1 2 3 4 5 
# Note: remember to increment i, or else the loop will continue forever.


i = 1
while i < 6:
	i += 1
	print(i)   # 2 3 4 5 6

# The break statement:
# With the break statement we can stop the loop even if the while condition is true:

# eg:Exit the loop when i is 3:

i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1            # 1 2 3

# The continue statement
# With the continue statement we can stop the current iteration, and continue with the next:

# eg:Continue to the next iteration if i is 3:

i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)        # 1 2 4 5 6

i = 1
while i < 6:
	i += 1
	
	if i == 3:
		break
	print(i)    # 2

# The else statement
# With the else statement we can run a block of code once when the condition no longer is true:

# eg:Print a message once the condition is false:

i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer than 6")


# It's best to illustrate the operating principle of a loop with a simple Python example. 
# The following small script calculates the sum of the numbers from 1 to 100.

m = 100
n = 0
i = 1
while i <= m:
	n += i
	i += 1
print("sum of 1 untill " + str(m) + " is " + str(n))


# for loop:
# ----------

''' A for loop is used for iterating over a sequence or datastructure (that is either a list, a tuple, a dictionary, a set, or a string).
    for loop will work along with a memebership operators(in, not in). for loop will take only one element from given datastructure 
    and assign it to the variable then python will execute block statement and continue with next iteration.
    This is less like the for keyword in other programming languages, and works more like an iterator method 
    as found in other object-orientated programming languages.

    With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''
# note: python will exit from for loop one's all the elements from the datastructures 'were'

''' syntax: for <variable> in <sequence>:
              <statements>
          else:
              <statements>'''

s = "helloworld"
for i in s:
	print(i)

l = [1, 2, 3, 4]
for i in l:
	if i % 2 == 0:
		print(i)

l = [1, 2, 3, 4]
for i in l:
	if i % 2 == 0 or i % 2 == 1:
		print(i)

l = ['hi', 'hello', 'world']
for i in l:
	
	if i == 'world':
		break
	print(i)         # hi
                     # hello


l = ['hi', 'hello', 'world']
for i in l:
	
	if i == 'world':
		break
print(i)                  # world



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break              # apple
                       # banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)            # apple




l = [1, 2, 3, 4]
op = []
for i in l:
	op.append(i**2)
print(op)               # [1, 4, 9, 16]

edibles = ["bacon", "spam", "eggs", "nuts"]
for food in edibles:
	if food == 'spam':
		print("No more spam please!")
		break
	print("Great, delicious " + food)

print("Finally, I finished stuffing myself")


edibles = ["bacon", "spam", "eggs", "nuts"]
for food in edibles:
	if food == 'spam':
		print("No more spam please!")
		continue
	print("Great, delicious " + food)

print("Finally, I finished stuffing myself")


# The range() function:
'''The built-in function range() is the right function to iterate over a sequence of numbers. 
   It generates an iterator of arithmetic progressions.'''

for i in range(5):
    print(i)

for i in range(4, 10, 2):
	print((i), end=' ')

# The range() function supplies the numbers from 1 to 100 for the for loop to calculate the sum of these numbers

n = 100
sum = 0
for i in range(1, n+1):
	sum += i
print('sum of 1 untill ' + str(n) + ' is ' + str(sum))


# If you have to access the indices of a list

a = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for i in range(len(a)):
	print(i, a[i])
print()


colours = ['red']
for i in colours:
	if i == 'red':
		colours += ['black']
	if i == 'black':
		colours += ['white']
print(colours) 


colours = ['red']
for i in colours[:]:
	if i == 'red':
		colours += ['black']
	if i == 'black':
		colours += ['white']
print(colours) 



'''1729 is the lowest number which can be represented by a Loeschian quadratic form a^2+ab+b^2  in four different ways, 
   with positive integers a and b .'''





import math

number = 1729
n = int(number ** (1/2))

results = {}
for a in range(n+1):
	for b in range(a):
		result = a ** 2 + a * b + b ** 2
		if result in results:
			results[result].append((a, b))
		else:
			results[result] = [(a, b)]
		if result > number:
			break

for x in results:
	if len(results[x]) > 3:
		print(x, results[x])




# l = [1, 2, 4, 3, 7, 9, 8, 6, 11, 12] write the even and odd elements in list

l = [1, 2, 4, 3, 7, 9, 8, 6, 11, 12]
even_list = []
odd_list = []

for i in l:
    if i % 2 == 0:
        even_list.append(i)
    else:
    	odd_list.append(i)
print(even_list, odd_list)

# cities = [("Tirupathi", "Metro"), ("Kadapa", "Non Metro"), ("Vizag", "Metro"), ("Chennai", "Metro"), ("Proddatur", "Non Metro")]
# to print the city name which are metro

cities = [("Tirupathi", "Metro"), ("Kadapa", "Non Metro"), ("Vizag", "Metro"), ("Chennai", "Metro"), ("Proddatur", "Non Metro")]

metro_cities = []

for i in cities:
	if i[1] == 'Metro':
		metro_cities.append(i)
	
print(metro_cities)


# w.a.p to sum the elements of the list

l = [1, 2, 3, 4]
op = 0
for i in l:
	op += i
print(op)

# 2nd method

l = [1, 2, 3, 4]
op = 0
for i in range(0,4):
	op += l[i]
print(op)


# w.a.p to sum 1 to 100 numbers

a = 1
n = 100
op = 0
for i in range(1, 101):
	op = op + i
print(op)

    
# w.a.p to print the numbers which are divisable by both 3 & 5

l = [3, 9, 15, 16, 30, 45, 12]
elements = []
for i in l:
    if i % 3 ==0 and i % 5 == 0:
    	elements.append(i)
print(elements)



''' range(): This method/function returns a sequence of numbers starting from 0(by default) and 
             increaments by 1(by default) and stops the before specified number.
             this method takes atleast one parameter and atmost three parameters.
             syntax: range(start, stop, step)

    input(): This function allows user input. atmost one parameter.
             syntax: input(prompt)

    enumerate(): This function takes a collection (eg: tuple) and returns it as an enumerate object.
                 This function adds a counter as the key of the enumerate object.
                 this function takes exactly two parameters
                 syntax: enumerate(iterable, start)'''

x = ('apple', 'banana', 'mango')
y = enumerate(x)
print(list(y))

''' sum(): This method returns a number the sum of all items in an iterable.
           This method takes atleast one parameter and atmost two parameters.
           syntax: sum(iterable, start)

a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)'''

''' max(): This function returns the item with the highest value or the item with the highest value in an iterable.
           If the values are strings an alphabetically comparison is done.
           This method takes atleast one parameter and atmost maximum parameters.
           syntax: max(n1, n2, ....) or max(iterable)'''

x = [1, 5, 4.9999]
print(max(x))

x = max("yeswanth", "akhil", "teja")
print(x)

''' min(): This function returns the item with the lowest value or the item with the lowest value in an iterable.
           If the values are strings an alphabetically comparison is done.
           This method takes atleast one parameter and atmost maximum parameters.
           syntax: min(n1, n2, ....) or min(iterable)'''

x = [1, 5, 4.9999]
print(min(x))

x = min("yeswanth", "akhil", "teja")
print(x)





# 