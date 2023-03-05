# Iterators:
# ----------

# Iterator is a small memory unit which is used to store one element at a time and reduce memory consumption.
# We acn use built in function called iter() to create an iterator.
# The output format is < data_structure object >

'''syntax:
          iterator_name = iter(data_structure)'''

l = [1, 2, 3, 4]
x = iter(l)
print(x)

# use built in function called next() to assist the data from iterator

print(next(x))
print(next(x))
print(next(x))
print(next(x))

l = [1, 2, 3, 4]
x = iter(l)
for i in x:
	print(i)

# note:
''' Iterators are used to reduce the memory consumption over the traditioal data_structure by the following the below the process.
    1) Traditional data_structure will consume all the memory for all the elements at a time.  irrespective of usage but in itteratos 
    the memory will be consume for the elements which worth access
    2) In iterators the elements will be deleted automatically once they are processed.'''



# Generators:
# -------------

# Generator will works like iterator but generator will also helps to inhance iteration control behaviour.
# To create a generator the combination of function along with yield keyword.
'''whenever yield keyword executed for the first time then python will create generator objet and the relevent data will get inserted 
   into generator object'''
# unlike returns yield statement will wait till all iterations were completed.


l = [1, 2, 3, 4, 5]
def even(l):
	for i in l:
		if i % 2 == 0:
			yield
x = even(l)
print(x)
print(next(x))
print(next(x))


# lambda functions:
# -----------------

# lambda functions are anonymous python in  which have a single statement i.e. responsible performming the operation.
# lambda function can be created with help of lambda keyword.
'''syntax:
          function_name = lambda p1, p2, p3, ............: operation'''

add = lambda a,b : a +b
print(add(10, 20))

# note:
''' The scope of lambda functions are very limited as be cannot implement multiple statements but they are powerful when 
    combining them with function programming tools
    donot the return keyword in lambda function'''


print(list(filter(lambda a: a % 2 == 0, [7, 8, 6, 11, 4])))

def even(a):
	if a % 2 == 0:
		return a
print(list(filter(even,[1, 2, 3, 4])))


def even(a):
	return a % 2 == 0
print(list(filter(even,[1, 2, 3, 4])))


# decorators:
# -------------

# decorators are wrapper(joining) functions which are used to implement new functionality without distrubing the base function.
# decorator function can be used on top of any function by using @decorator_name.
# To create custom decorator use the below syntax.
'''syntax:
          def decorator_name(base_function_name):    --------(3)
          	def wrapper(*args, **kwargs):            --------(5)
          		-------------------------
          		-------------------------
          		return base                          --------(6)
          	return wrapper                           --------(4)
          @decorator_name                            --------(2)
          def base(p1, p2, .......):                 --------(7)
          	-----------------------
          	-----------------------
          	print(base(value1, value2, ..........))   ------(1)'''


# The decorator function take exactly one parameter that is the base function name.
# The wrapper function take the set of parameter given to base function.


def check_type(f):
	def wrapper(a, b):
		if type(a) == int and type(b) == int:
			return f(a, b)
		else:
			return "invalid datatype"
	return wrapper
@check_type
def add(a, b):
	return a+b

print(add(10, 20))
print(add(10, 20.3))