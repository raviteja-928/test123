# list_comprehension:
# --------------------

# The process of creating a complex data list in a simple is known as list_comprehension.or
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# To perform the list comprehension our code should enclosed between two square braces.

# list_comprehension with two sections:
# ---------------------------------------

# syntax: [opertion section(2)      looping section(1)] 

l = [1, 2, 3, 4]
print([i **2 for i in l])  # [1, 4, 9, 6]

new_list = []
for i in l:
	a = i ** 2
	new_list.append(a)
print(new_list)

# list_comprehension with three sections:
# ---------------------------------------

# syntax: [operation section(3)    looping section(1)     condition section(2)]
#          newlist = [expression(3) for item in iterable(1) if condition == True(2)]


l = [3, 4, 8, 9, 11]
new_list = [i ** 2 for i in l if i % 2 == 0]
print(new_list)


op = []
for i in l:
	if i % 2 == 0:
		a = i ** 2
		op.append(a) # or op.append(i ** 2)
print(op)

# list_comprehension with four sections:
# --------------------------------------

# syntax: [operation True(3)    condition section(2)  operation False(4)  looping section(1)]

l = [1, 2, 3, 4, 5, 6]
print([i ** 2 if i % 2 == 0  else i ** 3  for i in l])

square_list = []
cube_list = []
for i in l:
	if i % 2 == 0:
		square_list.append(i ** 2)
	else:
		cube_list.append(i ** 3)



print(square_list, cube_list)


op = []
for i in l:
	if i % 2 == 0:
		op.append(i ** 2)
	else:
		op.append(i ** 3)
print(op)



# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
op = []
for i in fruits:
	if 'a' in i:
		op.append(i)
print(op)

# With list comprehension you can do all that with only one line of code:

op = [i for i in fruits if 'a' in i]
print(op)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[1] = "orange"
print(fruits)


for i in range(len(fruits)):
	if fruits[i] == 'banana':
		fruits[i] = 'orange'
print(fruits)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


l = [1, 1, 2, 6, 6, 8, 1, 2, 6, 8]
for i in range(len(l)):
	if l[i] in [1, 2, 6, 8]:
		l[i] = 3
print(l)

l = [1, 1, 2, 6, 6, 8, 1, 2, 6, 8]
for i in range(len(l)):
	if l[i] == 1:
		l[i] = 0
	elif l[i] == 2:
		l[i] = 3
	elif l[i] == 6:
		l[i] = 7
	elif l[i] == 8:
		l[i] = 9
print(l)

# w.a.p to find the number of occurrances of the elements

l = [1, 2, 3, 2, 4, 5, 5, 7, 2]
counts = dict()
for i in l:
	counts[i] = counts.get(i, 0) + 1
print(counts)

print({i:l.count(i) for i in l})

