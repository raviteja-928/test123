# Control Flow or Conditional Control Statements
# ----------------------------------------------

''' There comes situations in real life when we need to make some decisions and based on these decisions,
 we decide what should we do next. Similar situations arise in programming also where we need to make some decisions and 
 based on these decisions we will execute the next block of code.
 Decision-making statements in programming languages decide the direction of the flow of program execution.'''

''' In Python if, else, elif statement is used for decision making or Python supports three statements, 
 they are 1)if 2)if-else 3)if-else-ladder'''

# if statement:
# ................

''' if statement is the most simple decision-making statement. It is used to decide whether a certain statement or
 block of statements will be executed or not i.e if a certain condition is true then a block of statement is executed otherwise not.

Syntax: 


 if condition:
     # Statements to execute if condition is true

Here, the condition after evaluation will be either true or false. if the statement accepts boolean values – 
if the value is true then it will execute the block of statements below it otherwise not. We can use condition with bracket ‘(‘ ‘)’ also. 

As we know, python uses indentation to identify a block. So the block under an if statement will be identified as shown in the
 below example:  

if condition:
   statement1
statement2

# Here if the condition is true, if block  will consider only statement1 to be inside 
 its block.'''

# python program to illustrate If statement
# -----------------------------------------

i = 10
if(i > 15):
	print("10 is lessthn 15")
print("I am not in if")
# As the condition present in the if statement is false. So, the block below the if statement is executed.



# if-else:
# ----------

''' The if statement alone tells us that if a condition is true it will execute a block of statements and 
if the condition is false it won’t. But what if we want to do something else if the condition is false. 
Here comes the else statement. We can use the else statement with if statement to execute a block of code when 
the condition is false. 

Syntax: 

if (condition):
    # Executes this block if condition is true
else:
    # Executes this block if condition is false '''



# example1: python program to illustrate If else statement
# --------------------------------------------------------

i = 20
if (i < 15):
	print("i is smaller than 15")
	print("i am in if block")
else:
	print("i is greater than 15")
	print("i am in else block")

print("i am neither if or else block")

''' The block of code following the else statement is executed as the condition present in the if statement 
is false after calling the statement which is not in block(without spaces).'''

# Example 2: Python if else in list comprehension
# -----------------------------------------------

def digitsum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

list = [367, 111, 562, 945, 6726, 873]

new_list = [digitsum(i) for i in list if i & 1]
print(new_list)



# nested-if:
'''A nested if is an if statement that is the target of another if statement.
 Nested if statements mean an if statement inside another if statement.
  Yes, Python allows us to nest if statements within if statements. 
  i.e, we can place an if statement inside another if statement.'''

'''Syntax: 

if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here  '''

i = 10
if (i == 10):
    if (i < 15):
        print("i is smller than 15")
    if (i > 8):
        print("i is greaterthan 8")
    else:
        print("i is smaller than 15")



'''person = input("nationality is")
if person == Indian:
    print("person is")

age = int(input("the dog age is:"))
print()
if age < 0:
    print("This canot be True")
elif age == 0:
    print("This correspondent to 0 human years")
elif age == 1:
    print("This correspondent to 14 humn years")
elif age == 2:
    print("This roughly 22 years")
else:
    human = 22 + (age - 2) * 5
    print("correspondent" + str(human) + "human years")'''



inside_city_limits = True
if inside_city_limits:
    maximum_speed = 50
else:
    maximum_speed = 100
print(maximum_speed)





