# TypeCasting:
# ------------

# The process of converting the data from one type to another is known as TypeCasting.
# Use the below functios to convert the data into relevent format
# 1) int(): This metod returns given input data into integer type. syntax: int(data)

print(int(10.8))  # 10
print(int('10'))  # 10
# print(int('abc'))  # ValueError
# print(int[10, 0])  # TypeError
# print(int((1, 2)))  # TypeError

# 2) float():This metod returns given input data into float type. syntax: float(data)

print(float(10))  # 10.0
print(float('10'))  # 10.0
# print(float('abc'))  # ValueError
# print(float[10, 0])  # TypeError
# print(float((1, 2)))  # TypeError

# 3) str(): This metod returns given input data into string type. syntax: str(data)

print(str(10))  # 10
print(str(10.8))  # 10
print(str('abc'))  # abc
# print(str[1, 2])  # [1, 2]
print(str((1, 2)))  #  (1, 2)

# 4) list(): This metod returns given input data into list type. syntax: list(data) 

# print(list(10))  # TypeError
# print(list(10.8))  # TypeError
print(list('abc'))  # ['a', 'b', 'c']
print(list([10, 0]))  # [10, 0]
print(list((1, 2)))  # [1, 2]

# 5) tuple(): This metod returns given input data into tuple type. syntax: tuple(data)

# print(tuple(10))  # TypeError
# print(tuple(10.8))  # TypeError
print(tuple('abc'))  # ('a', 'b', 'c')
print(tuple([10, 0]))  # (10, 0)
print(tuple((1, 2)))  # [1, 2]



# DataManipulation:
# -----------------

# The process of altering(modification) the data is known as DataManipulation.
# As a part of data manipulation we can concatinate(addition), substraction, and multiplication one type of data with another

# concatination:

print(10 + 10)  # 20
print(10 + 10.8) # 20.8
# print(10 + '10') # TypeError
# print(10 + [10]) # TypeError
# print(10 + (10)) # TypeError

# Note: The concatination is only between different data types and in between a datastructure and integer
# Note: The multiplication is only possible between different data types and in between a datastructure and integer

print(10 * 10)
print(10.8 * 10.8)
print(10 * '10') 
print(10 * 10.8)
print(10 * [10])
print(10 * (10,20))

# print('10' * '20') # TypeError
# print([10] * '10')   # TypeError