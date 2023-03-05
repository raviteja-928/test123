# OOPS(Object Oriented Programming Structure):
# --------------------------------------------

# The group of objects will consider as a structure and forms an entity
# The major advantage of using oops is to provide the features like 1) security, 2) extendability, 3) reusability
# oops concepts are built based on two major components they are 1) class, 2) instance(object)

# 1) class:
# ---------

# The group of python objects that belongs to a specific entity is known as class
'''syntax:(create class)
          class ClassName:
          	-------------
          	-------------'''

# note:in class three components are there 1) name, 2) attributes/properties/data/variables, 3) functions/methods

class MyClass:
	x = 'Hello'
	y = [1, 2, 3]
	z = (4, 5, 6)

# 2) instance(object):
# --------------------

# object also called as instance of class
''' An instance is the reference of the class which is used to access the class property.
    syntax:(create an instance)
           instance = ClassName()'''

instance = MyClass()


# Accessing the properties from a class(Reading):
# -------------------------------------------------

'''syntax:
          instancename.propertyname'''

print(instance.x)
print(instance.y)

# Updating the class properties:
# ------------------------------

''' syntax:
           instancename.propertyname = new_value'''

instance.z = 10
print(instance.z)


# Inserting new property:
# -----------------------

'''syntax:
          instancename.newproperty = new_value'''

instance.a = {'a': 7, 'b': 8}
print(instance.a)

# Deleting property:
# -------------------

'''syntax:
          del instancename.propertyname

del instance.x
print(instance.x)'''

class MyClass:
	x = 100
	y = 200
	def add(a, b):
		return a + b
obj = MyClass()
print(obj.x)       
# print(obj.add(10, 20))        # TypeError: MyClass.add() takes 2 positional arguments but 3 were given

# self:
# -------

''' while calling a function /method python will internally pass the instance of the class as a first parameter , so we should
    use a special parameter to hold the instance of the class with in called function signature.
    In python self should be used as a first parameter in any class function
    Note:
    We can conclude that self is nothing but instance of the class properties from inside the class'''

class MyClass:
	x = 100
	y = 200
	def add(self,a, b):
		return a + b
obj = MyClass()
print(obj.x)       
print(obj.add(10, 20))



# example:create a first class

class Product:
	def __init__(self):
		self.name = 'Iphone'
		self.description = 'Its awesome'
		self.price = '700'
p1 = Product()
print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
print(p2.name)
print(p1.description)
print(p1.price)


# use parameterized constructor

class Course:
	def __init__(self, name, rating):
		self.name = name
		self.rating = rating

c1 = Course("Python", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.rating)

c2 =Course("Django", [1, 2, 3, 4, 5])
print(c2.name)
print(c2.rating)


# define a instance method

class Course:
	def __init__(self,name,rating):
		self.name = name
		self.rating = rating
	def average(self):
		numberofRatings = len(self.rating)
		average = sum(self.rating)/numberofRatings
		print("Average Ratings for", self.name, "is", average)
c1 = Course("Python", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.rating)
c1.average()

c2 = Course("Django", [4, 3, 5, 4.5, 3])
print(c2.name)
print(c2.rating)
c2.average()


# create getter(accessor) and setter(immitator) method

class Programmer:
	def setName(self,n):
		self.name = n
	def getName(self):
		return self.name

	def setSalary(self, sal):
		self.salary = sal
	def getSalary(self):
		return self.salary

	def setTechnologies(self, tech):
		self.technologies = tech
	def getTechnologies(self):
		return self.technologies

p1 = Programmer()
p1.setName('John')
p1.setSalary(15000)
p1.setTechnologies(["Python", "Django", "HTML"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())


# define instance methods/functions

class Product:
	def __init__(self):
		self.name = "Iphone"
		self.description = "It's awesome"
		self.price = 150000
	def display(self):
		print(self.name)
		print(self.description)
		print(self.price)

p1 = Product()
p1.display()

p2 = Product()
p2.display()


# Define static field

class Student:
    major = "CIVIL"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

s1 = Student(111, 'RaviTeja')
print(s1.major)
print(s1.rollno)
print(s1.name)
s2 = Student(112, 'Malli') 
print(s2.major)
print(s2.name)
print(s2.rollno)


# count the number of objects

class ObjectCounter:
	numberofobjects = 0
	def __init__(self):
		ObjectCounter.numberofobjects += 1
	@staticmethod
	def displaycount():
		print(ObjectCounter.numberofobjects)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displaycount()

# create a innerclass

class Car:
	def __init__(self, make, year):
		self.make = make
		self.year = year
class Engine:
	def __init__(self, number):
		self.number = number
	def start(self):
		print("Engine Started")

c = Car("BMW", 2016)
print(c.make)
print(c.year)
e = Engine(1452)
print(e.number)
e.start()


# Garbage collections:
# --------------------

# Garbage collector keeps running in the background as the part of python runtime it will clean up our objects when our program is done
# When the objects are no longer used. __del__ this method invokes clean up objects allocated memory.


# use destructor

class Product:
	def __init__(self):
		self.name = "Iphone"
		self.description = "It's awesome"
		self.price = 150000
	def __del__(self):
		print("Inside the destructor")

p1 = Product()
print(p1.name)
print(p1.description)
p1 = None

p2 = Product()
print(p2.name)
print(p2.description)
p2 = None


# patient clinicals usecase

class Patient:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.clinical = []

	def addClinicalData(self, clinical):
		self.clinical.append(clinical)

class clinical:
	def __init__(self,componentName, componentValue):
		self.componentValue = componentValue
		self.componentName = componentName

p = Patient("John", 28)
c1 = clinical("BP", "88/120")
p.addClinicalData(c1)
c2 = clinical("HeartRate",80)
p.addClinicalData(c2)

print(p.name)
print(p.age)
for eachclinical in p.clinical:
	print(eachclinical.componentName)
	print(eachclinical.componentValue)



# The four OOPS principles are 1) Encapsulation, 2) Inheritance, 3) Abstraction, 4) Polymorpism

# 1) Inheritance
# ------------

# The process of aquiring the data from one class to another is known as Inheritance.
# The class which provides the properties is known as Parent or Base class.
# The class in which we are accessing the properties is known as Child or Derived class.
'''Python provides five types of inheritane mechanisms. They are
   1) Single Inheritance
   2) Multiple Inheritance
   3) Hybrid Inheritance
   4) Hierachical Inheritance'''

# Another ddefiation:
# Inheritance is the process of defining a new object with the help of existing object
# Two important things in Inheritance i) Accessing existing objects functionality, ii) Updating existing objects functionality
# Inheritance are Re-usability and Is-A relation


# 1) Single Inheritance:
# ----------------------

# If the Inheritance involves one parent and one child class then it is known as Single Inheritance
'''syntx:
         class ClassName1:
         	-------------
         	-------------

         class ClassName2(ClassName1):
         	-------------------------
         	-------------------------'''

class A:
	x = 10
	y = 20
class B(A):
	z = 30
obj = B()
print(obj.z)
print(obj.x)
print(obj.y)


class BaseClass:
	a = 100
	b = 200
	def display(self):
		print("BaseClass")

class DerivedClass(BaseClass):
	x = 300
	y = 400
	def show(self):
		print("DerivedClass")

obj = DerivedClass()
print(obj.a)
print(obj.b)
obj.display()
print(obj.x)
print(obj.y)
obj.show()


# 2) Multiple Inheritance:
# ------------------------

# If the inheritance involves multiple parent(base) classes then it is known as Multiple Inheritance.
'''Python follows an order to execute the properties or methods which involves in inheritance. This order is known as 
   Method Resolution Order(MRO).
   According to MRO python will search for the properties in the class for which the instance has been created.
   If the property is not available then it will search in the inherited classes.[In the direction of left to right]
   syntax:
          class ClassName1:
          	--------------
          	--------------
          class ClassName2:
          	--------------
          	--------------
          class ClassName3(ClassName1, ClassName2):
          	---------------------------------------
          	---------------------------------------'''

class A:
	x = 10
class B:
	y = 20
class C(A, B):
	z = 30
obj = C()
print(obj.x)
print(obj.y)
print(obj.z)


class A:
	x = 10
	y = 35
	z = 45
class B:
	y = 60
	z = 70
	x = 80
class C(A, B):
	z = 90
	x = 85
	y = 75
obj = C()
print(obj.x)
print(obj.y)
print(obj.z)


class Father:
	def fdisplay(self):
		print("Father Class")
class Mother:
	def mdisplay(self):
		print("Mother Class")
class Child(Father, Mother):
	def cdisplay(self):
		print("Child Class")

family = Child()
family.fdisplay()
family.mdisplay()
family.cdisplay()


# 3) Multilevel Inheritance:
# --------------------------

'''syntax:
          class ClassName1:
          	---------------
          	---------------
          class ClassName2(ClassName1):
          	---------------------------
          	---------------------------
          class ClassName3(ClassName2:
          	--------------------------
          	--------------------------'''

class A:
	a = 10
	b = 20
	c = 30
class B(A):
	m = 40
	n = 50
	o = 60
class C(B):
	x = 70
	y = 80
	z = 90
obj = C()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.m)
print(obj.n)
print(obj.o)
print(obj.x)
print(obj.y)
print(obj.z)


class GrandParent:
	def gdisplay(self):
		print("GrandParent Class")

class Parent(GrandParent):
	def pdisplay(self):
		print("Parent Class")

class Child(Parent):
	def cdisplay(self):
		print("Child Class")

obj = Child()
obj.cdisplay()
obj.pdisplay()
obj.gdisplay()

obj1 = Parent()
obj1.gdisplay()


# 4) Hybrid Inheritance
# ---------------------

'''syntax:
          class A:
          	------
          class B(A):
          	--------
          class C(A):
          	--------
          class D:
          	------
          class E(C, D):
          	----------
          class F(E):
          	---------'''

# 5) Hierarchical Inheritance:
# ----------------------------

'''syntax:
          class A:
          	------
          class B(A):
          	--------
          class C(A):
          	--------
          class D(B):
          	---------
          class E(B):
          	--------
          class F(C):
          	--------
          class G(C):
          	--------'''



class BMW:
	def __init__(self, make, year, model):
		self.make = make
		self.year = year
		self.model = model

class ThreeSeries(BMW):
	def __init__(self, cruisecontrolenabled, make, year, model):
		self.cruisecontrolenabled = cruisecontrolenabled
		self.make = make
		self.year = year
		self.model = model

	def tdisplay(self):
		print("Starting The CAR")


class FiveSeries(BMW):
	def __init__(self, parkingassistenabled, make, year, model):
		self.parkingassistenabled = parkingassistenabled
		self.make = make
		self.year = year
		self.model = model

	def fdisplay(self):
		print("Starting The CAR")



obj = FiveSeries(True, "BMW", "2016", "320")
print(obj.parkingassistenabled)
print(obj.make)
obj.fdisplay()


# super():
# --------

# super is a built in function which will create and returns the instance of the parent class
# The major purpose of Super method is used to modify the Method Resolution Order(MRO).
'''syntax:
         super(class_name, self) or super()'''

class A:
	def add(self, a, b):
		return a + b
class B(A):
	def add(self, a, b):
		o = super() or super(B, self)
		print(o)
		print(o.add(a, b))
		return a * b
obj = B()
print(obj.add(10, 20))


# 2) Polymorphism:
# ----------------

''' The process of creating function which can perform multiple operations is known as Polymorphism or Implementing same thing in 
    different ways. for eg: area of polygon finding in different ways square(4sides), rectangle(4sides), triangle(3sides)
    Two types of Polymorphisms i) Compile time polymorphism (Implement with Method Overloading)
                               ii) Run time polymorphism (Implement with Method Overriding)'''

# i) Compile time polymorphism:
# -----------------------------

# This method is implement with method overloading 
# Method overloading is not support directly in python. It support with default parameters(default arguments and keyword arguments).

class Demo:
	def add(self):
		a = 10
		b = 20
		
	def add(self, a, b):
		print(a + b)
obj = Demo()
obj.add(100, 200)

class Demo:
	def add(self, a, b, c = 100):
		print(a + b + c)
obj = Demo()
obj.add(100, 200)
obj.add(100,200,300)


# ii) Run time polymorphism:
# --------------------------

# This method can implement with Method Overriding
# By using Inheritance method Parent(Base) class having methods override with Child(Derived) class methods.
# In Parent class any implementation is not satisfaction then that implementation we can do override.

class Parent:
	def transport(self):
		print("cycle")
class Child(Parent):
	def transport(self):
		print("byke")

c = Child()
c.transport()



# 3) Abstraction:
# -------------

# The process of hiding the data is known as Abstraction in python.
# Python uses the class name to bind with the property so the property will be hidden.
# To provide the abstraction use double under score(__) before the property name.
# The abstracted properties cannot be accessed directly with instance name insted use the below sytaxto access them
''' syntax:
           instance_name.__ClassName__propertyname'''

class A:
	x = 10
	__y = 200
obj = A
print(obj.x)
print(obj._A__y)


# abc(abstract base class) is module
# ABC(ABSTRACT CLASS) in abc module

from abc import ABC, abstractmethod  
class AbstractDemo(ABC):
	@ abstractmethod
	def HousingInterest(self):
		None
	@ abstractmethod
	def VehicleInterest(self):
		None

class SBI(AbstractDemo):
	def HousingInterest(self):
		print("Housing Interest 8.55")
	def VehicleInterest(self):
		print("Vehile Interest 5.55")

sbiobj = SBI()
sbiobj.HousingInterest()
sbiobj.VehicleInterest()

class Axis(AbstractDemo):
	def HousingInterest(self):
		print("Housing Interest 8.05")
	def VehicleInterest(self):
		print("Vehile Interest 5.05")

axisobj = Axis()
axisobj.HousingInterest()
axisobj.VehicleInterest()



# 4) Encapsulation and Data hiding
# -----------------------------

# The process of binding(wrapping or joining) the data/attributes/parameters/variables and methods/functions is known as Encapsulation.
# In python both abstraction and encasulation i work in same way.(There are no technical difference between them)

# Data hiding means give the security to data
# Security will be given with Access Specifiers.
# Access specifiers are Public (with in class and outside class variable and methods access do it ) and Private(only with in class)
# __variable ------> Private variable  &   __method-------> Private method
# variable --------> Public variable   &   method---------> Public method


class Demo:
	__a = 10
	b = 100

	def display(self):
		print("Display Method In Demo Class")
obj = Demo()
print(obj._Demo__a)
print(obj.b)
obj.display()



# Constructor:
# ------------

# Constructor is a special(magical) function in python which will get executed automatically when an instance created for the class
# __init__() will considered as a constructor
# The major purpose of constructor is used to create and access the other class properties.
# It is also used to define the prerequired data which can be used in other class properties.

class A:
    x = 10
    def __init__(self):
        print("I am Constructor")
    def add(self, a, b):
        return a + b
obj = A()
print(obj.add(10, 20))


# Destructor:
# -----------

'''A Destructor is a special(magical) function/method in python which will get all references to an object have been destroyed
   or deleted automatically.
   __del__() method cosidered as a destructor.'''


class A:
    x = 10
    def __init__(self):
        print("I am student")
    def __del__(self):
    	print("The destructor is called. I am student is deleted")
        
obj = A()
del obj



# Method Overloading:
# -------------------

# The process of creation two or more functions with same function name and with differnt signature is known as Method Overloading.
# Due to memory limitation of python we cannot create multiple functions with same name.
# But we cannot acheive the features of method overloading by using the default parameter.
'''Note: 
   Multiple dispatch:(not in real time)
   We can override an method overloading by using module name at multiple dispatch.
   eg: dispatch(int, int)
       def add(a, b):'''


# Method Overriding:
# ------------------

# The process of creating two or more functions with same function name and with same signature is known as Method Overriding.
# Due to python memory limitation we cannot acheive Method Overriding directly.
# To acheive the features of metod overriding we should place those function in different class.
# In the multiple functions having different set of logical statemet they will be able to perform multiple operations.
# If single function is able to perform multiple operation. The function will consider as polymorphism.
# The process of creating function. Which can perform multiple operations is known as Polymorphism.

class A:
	def add(self, a, b):
		return a + b
class B:
	def add(self, a, b):
		return a * b
obja = A()
print(obja.add(10, 20))
objb = B()
print(objb.add(10, 20))



# Cyclic redundancyissue or Diamond Inheritance issue:
# ----------------------------------------------------

# The scope of multiple inheritance is limited as it may result cyclic redundancy issue or diamond inheritace issue.
# The state where python is not capable to fetch(decide) the properties is known as Diamond inheritnce issue.  


# Instance Methods:
# -----------------

# The method which can be access with help instance only.
# Instance method should contain "self" as default parameter.

# @classmethod:
# ------------
# The method which can be access with help of either class name or instance.
# use '@classmethod' decorator to create class methods.
# classmethod should contain "cls" as default list parameter.

# @staticmethod:
# --------------

# The method available in a class but cannot communicate with other class property is known as static method.
# To create a static method use '@staticmethod' decorator.
# No need to use any default list parameter like 'self' or 'cls'.
# staticmethod can also be access with help of either class name or instance.
